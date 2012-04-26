<h2>Problem 3: Simple Database</h2>
<p>Your task is create a very simple database, which has a very limited command set.  We aren't going to be storing that much data, so you don't have to worry about storing anything on disk; in-memory is fine.  All of the commands are going to be fed to you one line at a time via stdin, and your job is the process the commands and perform whatever operation the command dictates.  Here are the basic commands you need to handle:</p>
<ul>
<li><strong>SET [name] [value]</strong>: Set a variable [name] to the value [value].  Neither variable names or values will ever contain spaces.</li>
<li><strong>GET [name]</strong>: Print out the value stored under the variable [name].  Print NULL if that variable name hasn't been set.</li>
<li><strong>UNSET [name]</strong>: Unset the variable [name]
<li><strong>EQUALTO [value]</strong>: Return all variables equal to [value].  The variables should be sorted in alphabetical order.  Output "NONE" if no variables are equal.</li>
<li><strong>END</strong>: Exit the program
</ul>
<p>So here is a sample input:</p>
<pre>
SET a 10
GET a
UNSET a
GET a
END
</pre>
<p>And its corresponding output:</p>
<pre>
10
NULL
</pre>
<hr style="width:200px">
<p>And another one:</p>
<pre>
SET a 10
SET b 10
EQUALTO 10
EQUALTO 20
UNSET a
EQUALTO 10
SET b 30
EQUALTO 10
END
</pre>
<p>And its corresponding output:</p>
<pre>
a b
NONE
b
NONE
</pre>
<p>Now, as I said this was a database, and because of that we want to add in a few transactional features to help us maintain data integrity.  So there are 3 additional commands you will need to support:</p>
<ul>
<li><strong>BEGIN</strong>: Open a transactional block</li>
<li><strong>ROLLBACK</strong>: Rollback all of the commands from the most recent transaction block.  If no transactional block is open, print out INVALID ROLLBACK</li>
<li><strong>COMMIT</strong>: Permanently store all of the operations from any presently open transactional blocks</li>
</ul>
<p>Our database supports nested transactional blocks as you can tell by the above commands.  Remember, ROLLBACK only rolls back the <i>most recent transaction block</i>, while COMMIT closes <i>all open transactional blocks</i>.  Any command issued outside of a transactional block commits automatically.</p>
<p>
Even though we aren't dealing with a ton of data, we still want to use
memory efficiently. Typically, we will already have committed a lot of data
when we begin a new transaction, but the transaction will only modify a few
values. So, your solution should be efficient about how much memory is
allocated for new transactions, i.e., it is bad if beginning a transaction
nearly doubles your program's memory usage.
</p>
<p>Here are some sample inputs and expected outputs using these commands:</p>
<p><strong>Input:</strong></p>
<pre>
BEGIN
SET a 10
GET a
BEGIN
SET a 20
GET a
ROLLBACK
GET a
ROLLBACK
GET a
END
</pre>
<p><strong>Output:</strong></p>
<pre>
10
20
10
NULL
</pre>
<hr style="width:200px">
<p><strong>Input:</strong></p>
<pre>
BEGIN
SET a 30
BEGIN
SET a 40
COMMIT
GET a
ROLLBACK
END
</pre>
<p><strong>Output:</strong></p>
<pre>
40
INVALID ROLLBACK
</pre>
<hr style="width:200px">
<p><strong>Input:</strong></p>
<pre>
SET a 50
BEGIN
GET a
SET a 60
BEGIN
UNSET a
GET a
ROLLBACK
GET a
COMMIT
GET a
END
</pre>
<p><strong>Output:</strong></p>
<pre>
50
NULL
60
60
</pre>
<hr style="width:200px">
<p><strong>Input:</strong></p>
<pre>
SET a 10
BEGIN
EQUALTO 10
BEGIN
UNSET a
EQUALTO 10
ROLLBACK
EQUALTO 10
END
</pre>
<p><strong>Output:</strong></p>
<pre>
a
NONE
a
</pre>
