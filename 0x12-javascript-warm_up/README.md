Here's the formatted README file for your project:

```markdown
# JavaScript Project

## Background Context

JavaScript is a versatile language used for both scripting and web development. In this project, you'll explore JavaScript for two main purposes:

- **Scripting:** Similar to Python, JavaScript can be used to create scripts that automate tasks or interact with external programs.

- **Web Front-End:** JavaScript plays a crucial role in enhancing the interactivity and dynamic nature of web pages.

To begin, you'll focus on the basics of JavaScript, including variables, data types, operators, control flow statements, functions, objects, and arrays. Later, you'll apply these concepts to build dynamic web pages using JavaScript and jQuery.

## Learning Objectives

By the end of this project, you'll be able to:

- Explain the significance and benefits of JavaScript programming
- Execute JavaScript scripts using the Node.js interpreter
- Create and manipulate variables and constants using `var`, `const`, and `let`
- Work with various data types in JavaScript, including numbers, strings, booleans, objects, and arrays
- Employ `if`, `if...else` statements for conditional branching
- Leverage comments to enhance code readability and documentation
- Assign values to variables effectively
- Utilize `while` and `for` loops for repetitive tasks
- Implement `break` and `continue` statements for control flow management
- Understand the concept of functions and their usage in programming
- Comprehend the default return value of a function without an explicit `return` statement
- Explore variable scope and its implications for program behavior
- Utilize arithmetic operators for mathematical operations
- Manipulate dictionaries (objects) effectively
- Import external JavaScript files for code modularity

## More Info

**Install Node 14**

```bash
$ curl -sL [https://deb.nodesource.com/setup_14.x](https://deb.nodesource.com/setup_14.x) | sudo -E bash -
$ sudo apt-get install -y nodejs
```

**Install semi-standard**

```bash
$ sudo npm install semistandard --global
```

**Documentation**

[semistandard](https://github.com/lodash/semistandard/blob/master/README.md)

**Quiz questions**

Great! You've completed the quiz successfully! Keep going! (Show quiz)

## Tasks

### 0. First constant, first print

**mandatory**

Write a script that prints "JavaScript is amazing".

* You must create a constant variable called `myVar` with the value "JavaScript is amazing"
* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```javascript
const myVar = "JavaScript is amazing";
console.log(myVar);
```

**Expected output:**

```
JavaScript is amazing
```

### 1. 3 languages

**mandatory**

Write a script that prints 3 lines:

* The first line: "C is fun"
* The second line: "Python is cool"
* The third line: "JavaScript is amazing"

* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```javascript
console.log("C is fun");
console.log("Python is cool");
console.log("JavaScript is amazing");
```

**Expected output:**

```
C is fun
Python is cool
JavaScript is amazing
```

### 2. Arguments

**mandatory**

Write a script that prints a message depending of the number of arguments passed:

* If no arguments are passed, print "No argument"
* If only one argument is passed, print "Argument found"
* Otherwise, print "Arguments found"

* You must use `console.log(...)` to print all output
* You are not allowed to use `var`

```javascript
console.log(process.argv);
```

**Expected output:**

```
0 arguments
```

```javascript
console.log(process.argv[1]);
```

**Expected output:**

```
1 argument
```

```javascript
console.log(process.argv[1]);
// or
console.log("First argument:", process.argv[1]);
```

**Expected output:**

```
2 arguments
```

**Note:** You are not allowed to use `length` in this task.

### 3. Value of my argument

Write a script that prints the first argument passed to it ...
