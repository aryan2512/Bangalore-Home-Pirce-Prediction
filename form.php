<!DOCTYPE html>
<html>
<body>

<h2>HTML Forms</h2>

<form action="<?php echo $_SERVER['PHP_SELF'] ?>" method="post">
  <label for="fname">First name:</label><br>
  <input type="text" id="fname" name="fname" value="John"><br>
  <label for="lname">Last name:</label><br>
  <input type="text" id="lname" name="lname" value="Doe"><br><br>
  <input type="submit" name="submit" value="Submit">
</form>

<p>If you click the "Submit" button, the form-data will be sent to a page called "/action_page.php".</p>

<?php
    if(isset($_POST['submit']))
    {
      $fname= $_POST['fname'];
      $lname= $_POST['lname'];
      $conn= mysqli_connect("localhost","root","","test") or die("connection fail");
      $sql= "insert into student (fname,lname) values ('{$fname}','{$lname}')";
      if(mysqli_query($conn,$sql))
      {
        header('location: http://localhost/PHP/practice/form.php');
      }
    mysqli_close($conn);
    }
 ?>
</body>
</html>
