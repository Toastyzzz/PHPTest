<!DOCTYPE html>
<html>
<head>
    <title>PHP Input Example</title>
</head>
<body>

<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]); ?>">
    Enter your name: <input type="text" name="username">
    <input type="submit" value="Submit">
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the input value and sanitize it
    $name = htmlspecialchars($_POST["username"]);
    echo "<h3>Hello, " . $name . "!</h3>";
}
?>

<?php
    echo "<h1>Test Message</h1>";
?>

</body>
</html>
