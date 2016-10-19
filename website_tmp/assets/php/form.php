
<?php
if(isset($_POST['email'])) {
     
    // CHANGE THE TWO LINES BELOW
    $email_wien = "wien@smartrep.com";
    $email_zuerich = "msolar@ethz.ch";
     
    $email_subject = "Smartrep php Form";
     
     
    function died($error) {
        // your error code can go here
        echo "We are very sorry, but there were error(s) found with the form you submitted. ";
        echo "These errors appear below.<br /><br />";
        echo $error."<br /><br />";
        echo "Please go back and fix these errors.<br /><br />";
        die();
    }
     
    // validation expected data exists
    if(!isset($_POST['name']) ||
        !isset($_POST['email']) ||
        !isset($_POST['subject']) ||
        !isset($_POST['message'])) {
        died('We are sorry, but there appears to be a problem with the form you submitted.');      
    }
     
    $name = $_POST['name']; // required
    $email_from = $_POST['email']; // required
    $subject = $_POST['subject']; // not required
    $message = $_POST['message']; // required
     
    $error_message = "";
    $email_exp = '/^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$/';
  if(!preg_match($email_exp,$email_from)) {
    $error_message .= 'The Email Address you entered does not appear to be valid.<br />';
  }
    $string_exp = "/^[A-Za-z .'-]+$/";
  if(!preg_match($string_exp,$name)) {
    $error_message .= 'The First Name you entered does not appear to be valid.<br />';
  }
  if(strlen($message) < 10) {
    $error_message .= 'The message you entered do not appear to be valid.<br />';
  }
  if(strlen($error_message) > 0) {
    died($error_message);
  }
  if(!isset($_POST['standortDE'])  &&  !isset($_POST['standortCH'])  &&  !isset($_POST['standortCH'])) {
    $error_message .= 'Bitte wählen Sie Ihren Standort.<br />';
    echo "keine checkbox";
  }

    $email_message = "Form details below.\n\n";
     
    function clean_string($string) {
      $bad = array("content-type","bcc:","to:","cc:","href");
      return str_replace($bad,"",$string);
    }
     
    $email_message .= "Name: ".clean_string($last_name)."\n";
    $email_message .= "Email: ".clean_string($email_from)."\n";
    $email_message .= "subject: ".clean_string($subject)."\n";
    $email_message .= "message: ".clean_string($message)."\n";
     

// create email headers
$headers = 'From: '.$email_from."\r\n".
'Reply-To: '.$email_from."\r\n" .
'X-Mailer: PHP/' . phpversion();

print_r($_POST['standortDE']);

if(isset($_POST['standortDE'])  || isset($_POST['standortCH'])) {

	@mail($email_zuerich, $email_subject, $email_message, $headers); 

} elseif (isset($_POST['standortOE'])) {

	@mail($email_wien, $email_subject, $email_message, $headers); 

}
	
?>
 
<!-- place your own success html below -->
 
Thank you for contacting us. We will be in touch with you very soon.
 
<?php
}
die();
?>