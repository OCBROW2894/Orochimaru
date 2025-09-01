<h1>Functions and Loops</h1>
<p>
 - <b><i>del</i></b> - is a keyword used to un-assign a variable name from a value <br>
 - An <b>Argument</b> - is a value that gets <i><b>passed</b></i> to the function as input
</p>
<p>
 <img width="703" height="275" alt="image" src="https://github.com/user-attachments/assets/cc09ca99-236c-48fe-803b-1703f3ec2fbb" /> <br>
 - A <b><i>Side Effect</i></b> - is when a function affects something external to the function itself <br>
 - When you call <b><i>print()</i></b>, the things that gets displayed is not the return value. It's the side effect of <i>print()</i>
</p>
<p>
 <img width="740" height="227" alt="image" src="https://github.com/user-attachments/assets/3b5b7a17-0f66-4eba-b1e4-cef14c26a74a" /> <br>
<img width="675" height="117" alt="image" src="https://github.com/user-attachments/assets/e76bfbfb-991b-4dc5-9fd7-a52169dc76f5" /> <br>
The <i><b>Function Signature</b></i> has 4 parts: <br>
1. The <i>def</i> keyword <br>
2. The function <i>name</i> <br>
3. The arguments, <i>(x, y)</i> <br>
4. A colon <i>(:)</i> at the end of the line <br>
The <i><b>Function Body</b></i> is the code that gets run whenever the function is used in your program <br>
 <b>NOTE:-</b> A <b><i>Container</i></b> is a special name for an object that contains other objects <br>
 - A <b><i>Docstring</i></b> Is a triple-quoted string literal placed at the top of the function body
</p>
<p>
 <h3>Run In Circles</h3>
 - A <b>Loop</b> is a block of code that gets repeated over and over again until a certain conditions is met <br>
 <img width="693" height="282" alt="image" src="https://github.com/user-attachments/assets/bcdf2b90-774a-4640-9249-ce6d502ea76a" /> <img width="267" height="271" alt="image" src="https://github.com/user-attachments/assets/65120501-5d58-407d-a59a-52c36e074be0" /> <img width="726" height="356" alt="image" src="https://github.com/user-attachments/assets/9379596b-9ba8-4d0c-8acd-4361b0bf7c25" />
</p>
<p>
 <h3>Understand scope in python</h3>
 <img width="733" height="373" alt="image" src="https://github.com/user-attachments/assets/991e1453-e9fe-4466-a244-70d5d71ea773" /> <br>

<h4>The LEGB Rule</h4>
A useful way to remember how Python resolves scope is with the
 <b>LEGB</b> rule. This rule is an acronym for <b>L</b>ocal, <b>E</b>nclosing, <b>G</b>lobal, <b>B</b>uilt-in. <br>
 <img width="736" height="502" alt="image" src="https://github.com/user-attachments/assets/8304db2b-6af4-4d20-8c19-7391229dc8e5" />

</p>
<p>
 <h2>Additional content</h2>
 <h3>Python while Loops: Repeating Tasks Conditionally</h3>
 <h4>Using Advanced While Loop Syntax</h4>
 - <b><i>break:</i></b> Immediately terminates a loop. The program execution then proceeds with the first statement following the loop body.
 - <b><i>continue:</i></b>  Ends only the current iteration. The execution jumps back to the loop header, and the loop condition is evaluated to determine whether the loop will execute again.
 - <b><i>else:</i></b> The code under the else clause will run only if the while loop terminates naturally without encountering a break statement. In other words, it executes when the loop condition becomes false, and only then. <br>
<b><i>Note that it doesn’t make much sense to have an else clause in a loop that doesn’t have a break statement. In that case, placing the else block’s content after the loop—without indentation—will work the same and be cleaner.</i></b>
</p>


