# Conditional Logic and Control Flow
- <b>Uncondtional</b> - Code that does not make any choices <br>
- <b><i>Conditional Logic</i></b> - programs that perform different actions based on different conditions <br>

<img width="646" height="266" alt="image" src="https://github.com/user-attachments/assets/12890522-9981-4f56-88d0-2306601ce796" />

Strings are ordered <b><i>Lexicographically</i></b>, which is a fancy way to say they are ordered as they would appear in a dictionary
<p>
  
### Add Some Logic
#### AND
  <img width="338" height="193" alt="image" src="https://github.com/user-attachments/assets/d6941ebb-9a36-4215-97d7-296d7ab7f37e" />

#### OR
<img width="323" height="190" alt="image" src="https://github.com/user-attachments/assets/5616dbba-8ea4-4c1e-8d5f-dc83f0635969" />

#### NOT
<img width="577" height="150" alt="image" src="https://github.com/user-attachments/assets/a978c1b9-983c-4392-8a43-f2407e7ecdd1" /> <br>

<img width="507" height="190" alt="image" src="https://github.com/user-attachments/assets/8a855efd-d4fe-4515-b94c-1ba7f7b3dc48" />

</p>
<p>
  
### Control the Flow of Your Program
- <b><i>if</i></b> :- An if statement tells Python to only execute a portion of code if a condition is met <br>
- <b><i>else</i></b> :- The else keyword is used after an if statement in order to execute some code only if the if statement’s test condition is False <br>
  <img width="676" height="89" alt="image" src="https://github.com/user-attachments/assets/6ddb1bf8-f3ca-4f4d-bd0a-9444e2549202" /> <br>

- <b><i>elif</i></b> :- Theelifkeywordisshortfor“elseif”andcanbeusedtoaddadditional
 conditions after an if statement <br>
  <img width="679" height="197" alt="image" src="https://github.com/user-attachments/assets/983edfe3-5867-4d5b-96b0-33c68472fa47" />

</p>
<p>
  
### Break out of the pattern
- <b><i>break</i></b> - Thebreak keyword tells Python to literally break out of a loop. That is, the loop stops completely and any code after the loop is executed. <br>
- <b><i>continue</i></b> - The continue keyword is used to skip any remaining code in the loop body and continue on to the next iteration.
  
### Recover from Errors
  <img width="684" height="84" alt="image" src="https://github.com/user-attachments/assets/8ed750aa-ed6b-4650-a19c-1d362612b474" />

#### A Zoo of Exceptions
- <b><i>ValueError</i></b> - A ValueError occurs when an operation encounters an invalid value. <i> For example, trying to convert the string "not a number" to an integer results in a ValueError</i> <br>
- <b><i>TypeError</i></b> - A TypeError occurs when an operation is performed on a value of the wrong type. <i> For example, trying to add a string and an integer will result in a TypeError:</i> <br>
- <b><i>NameError</i></b> - A NameError occurs when you try to use a variable name that hasn’t been defined yet <br>
- <b><i>ZeroDivisionError</i></b> - A ZeroDivisionError occurs when the divisor in a division operation is 0 <br>
- <b><i>OverFlowError</i></b> - An OverflowError occurs when the result of an arithmetic operation is too large. <i>For example, trying to raise the value 2.0 to the power 1_000_000 results in an OverflowError</i> <br>
- <b><i>IndexError</i></b> - when  string index out of range, for example <i>The user tried to get an index of a string but enters a number > len(string)</i>

<h4>THE "BARE" except CLAUSE</h4>
<img width="684" height="125" alt="image" src="https://github.com/user-attachments/assets/cd39c179-943c-4525-b9e4-4ddb6b778c3b" /> <br>
<p>
  This might sound like a great way to ensure your program never crashes, <b><i>but this is actually bad idea and the pattern is generally frowned upon!</i></b> <br>
  There are a couple of reasons for this, but the most important reason for new programmers is that catching every exception could hide bugs in your code, giving you a false sense of confidence that your code works as expected.
</p>

</p>
<p>
  The Wikipedia page on the [Monte Carlo method](https://en.wikipedia.org/wiki/Monte_Carlo_method) provides a comprehensive overview of this powerful computational technique. Here's a concise summary:

### 🧠 What Is the Monte Carlo Method?
- A class of algorithms that use repeated random sampling to solve problems.
- Named after the Monte Carlo Casino due to its reliance on randomness.
- Useful for problems that are deterministic but too complex to solve analytically.

### 🔍 Core Applications
- **Optimization**: Finding best solutions under constraints.
- **Numerical Integration**: Estimating integrals, especially in high dimensions.
- **Probability Distribution Sampling**: Generating random samples from complex distributions.

### 🧪 How It Works
1. Define a domain of possible inputs.
2. Randomly generate inputs from a probability distribution.
3. Perform deterministic computations.
4. Aggregate results to approximate the solution.

### 📌 Example
- Estimating π by randomly placing points in a square and counting how many fall inside a quadrant of a circle.

### 🛠️ Advanced Techniques
- **Markov Chain Monte Carlo (MCMC)**: Samples from complex distributions using Markov chains.
- **Mean-field particle methods**: Use interacting particles to simulate nonlinear processes.

### ⚠️ Limitations
- High computational cost.
- Curse of dimensionality.
- Dependence on quality of random number generators.

### 🌍 Fields of Use
- Physics, chemistry, biology, finance, AI, engineering, climate science, law, and even library science.
- Widely used in simulations, risk analysis, game AI (e.g., Monte Carlo Tree Search), and rendering in computer graphics.

### 🕰️ Historical Origins
- Developed in the 1940s by Stanisław Ulam and John von Neumann during nuclear weapons research.
- Evolved through contributions in physics, statistics, and computational science.

</p>

<p>
  
### A Module
- A <b><i>module</i></b> is a collection of related code. Python’s <b><i>standard library</i></b> is an organized collection of modules that you can <b><i>import</i></b> into your own code in order to solve various problems.
</p>
