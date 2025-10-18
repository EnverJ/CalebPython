# Title 
## Title
### Title


## Syntax Highlighting
```python
name = input()
print("Hello", name)
```
An `inline` code highlight
## Comments

[This is my comment]: # 

<!-- This is an HTML --->

## Understanding new Line
this 
is not
multiple 
lines

This  
is  
multiple  
lines.

## Bold and Italics
You can make something _italicized_.
You can make something **Bold**


## lINKS
Check out my [new site](www.google.com).  
Check out my [new site](#comments).

## Images
![Alt text](desktop.png)

## Lists 
1. This
2. Will
3. Always


## Block Quotes
> this is an Block Quotes


## Tables
|Syntax|Descriptions|

## Checkboxes
- [x] Done

## Horizontal Dividers

----
This is a section
----

## Emoji Shortcuts
:joy:


## Highlighting
This === dose not ===work

## HTML in Markdown


<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Login Page</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f0f2f5;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
    }
    .login-container {
      background: #fff;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.15);
      width: 300px;
      text-align: center;
    }
    h2 {
      margin-bottom: 20px;
    }
    .input-group {
      margin-bottom: 15px;
      text-align: left;
    }
    label {
      font-size: 14px;
      display: block;
      margin-bottom: 5px;
    }
    input {
      width: 100%;
      padding: 10px;
      border-radius: 6px;
      border: 1px solid #ccc;
      font-size: 14px;
    }
    button {
      width: 100%;
      padding: 12px;
      background: #007bff;
      border: none;
      color: #fff;
      font-size: 16px;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.3s;
    }
    button:hover {
      background: #0056b3;
    }
    .extra-links {
      margin-top: 15px;
      font-size: 14px;
    }
    .extra-links a {
      color: #007bff;
      text-decoration: none;
    }
    .extra-links a:hover {
      text-decoration: underline;
    }
  </style>
</head>
<body>
  <div class="login-container">
    <h2>Login</h2>
    <form action="/login" method="post">
      <div class="input-group">
        <label for="username">Username</label>
        <input type="text" id="username" name="username" required>
      </div>
      <div class="input-group">
        <label for="password">Password</label>
        <input type="password" id="password" name="password" required>
      </div>
      <button type="submit">Log In</button>
    </form>
    <div class="extra-links">
      <p><a href="#">Forgot Password?</a></p>
      <p><a href="#">Create an Account</a></p>
    </div>
  </div>
</body>
</html>