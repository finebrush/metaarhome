// Attach an event for when the user submits the form
$('#contact-form').on('submit', function(event) {

    // Prevent the page from reloading
    event.preventDefault();

    // Set the text-output span to the value of the first input
    // var $input = $(this).find('input');
    // var input = $input.val();
   var qaname = $("#form_name").val();
   var qaemail = $("#form_email").val();
   var qamessage = $("#form_message").val();
   var totalmessage = '[이름]==>'+qaname+'\n.....'+'[이메일]=>'+qaemail+'\n.....'+'[문의내용]=>'+qamessage
   // $('#text-output').text("You typed: " + totalmessage);
   qaurl = "https://api.telegram.org/bot648414359:AAGhhCZlAe7DTL8tvBUvrFC5vj-TQW-g5fY/sendMessage?chat_id=28713807&text="
   $.get( qaurl+totalmessage, function(jqXHR) {
       alert( "success" );
   }, 'json' /* xml, text, script, html */)
   .fail(function(jqXHR) {
       alert( "error" );
   });
   //document.getElementById("contact-form").reset(); // 폼 전체 비우기
   document.getElementById("form_message").value = ""; // 폼안의 특정 필드만 지우기
});
