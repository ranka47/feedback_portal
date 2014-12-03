$(document).ready(function(){
//  Check Radio-box
    $("input:radio").attr("checked", false);
    $('input').click(function () {
        $("span").removeClass('checked');
        $(this).parent().addClass('checked');
    });

    $('input:radio').change(
    function(){
        var userRating = this.value;
        //alert(userRating);

        // send this userRating variable to calculate the rating of the prof
    });

});


function rb_too_low(){
  document.getElementById('too_low_level').style.display="block";
  document.getElementById('too_high_level').style.display="none";
}

function rb_intermediate(){
  document.getElementById('too_low_level').style.display="none";
  document.getElementById('too_high_level').style.display="none";
}

function rb_too_high(){
  document.getElementById('too_low_level').style.display="none";
  document.getElementById('too_high_level').style.display="block";
}

function rb_theoretical(){
  document.getElementById('too_theoretical_expectations').style.display="block";
}

function rb_noe(){
  document.getElementById('too_theoretical_expectations').style.display="none";
}

function rb_inst_clear(){
  document.getElementById('why_not').style.display="none";
}

function rb_inst_notclear(){
  document.getElementById('why_not').style.display="block";
}

function tut_helpful(){
  document.getElementById('reasons').style.display="none";
}

function tut_not_helpful(){
  document.getElementById('reasons').style.display="block";
}
// when submit button is clicked
// $( "#target" ).submit(function() {
//     $('input:radio:checked').each(function() {
//     // Iterate through all checked radio buttons
//     total = total + parseInt(this.value);
//     });
//     alert(total);
// });


// function getTotal() {
//     $('input:radio:checked').each(function() {
//     // Iterate through all checked radio buttons
//     total = total + parseInt(this.value);
//     });
//     alert(total);
// }
function getTotal1() {
    var total=0;
    var total1 = 0;
    var total2 = 0;
    var total3 = 0;
    var total4 = 0;
    var count=0;
    $("input:radio:checked").each(function() {
    // Iterate through all checked radio buttons
    if (count < 6) {
        total1 = total1 + parseInt(this.value);
        document.getElementById('id_mid_design_value').innerHTML = total1;
        count = count + 1;
    }
    else if (count >= 6 && count < 12) {
        total2 = total2 + parseInt(this.value);
        document.getElementById('id_mid_instructor_value').innerHTML = total2;
        count = count + 1;
    }
    else if(count >= 12 && count < 16) {
        total3 = total3 + parseInt(this.value);
        document.getElementById('id_mid_tutorial_value').innerHTML = total3;
        count = count + 1;
    }
    else {
        total4 = total4 + parseInt(this.value);
        document.getElementById('id_mid_exam_value').innerHTML = total4;
        count = count + 1;
    }

});

    document.getElementById('id_mid_design_value').value = total1;
    document.getElementById('id_mid_instructor_value').value = total2;
    document.getElementById('id_mid_tutorial_value').value = total3;
    document.getElementById('id_mid_exam_value').value = total4;



    var msg= "Some comments about the course:";
    var inputElements = document.getElementsByName('poll13a');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].checked){
           msg = msg.concat("\n->".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll13b');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].checked){
           msg = msg.concat("\n->".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll13tb');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('topic_suggestion');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('implementation_change');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->Changes to the implementation: ".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('more_emperical_approach');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->Topics that need a more empirical approach: ".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll21a');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].checked){
           msg = msg.concat("\n->Instructor was not clear due to: ".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll21atb');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->Instructor was not clear due to: ".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll31a');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].checked){
           msg = msg.concat("\n->Tutorials were not helpful because: ".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll31atb');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->Tutorials were not helpful because: ".concat(inputElements[i].value));
      }
    }
    msg = msg.concat("\nPlease take measures to improve on these.");

    document.getElementById('id_post').value = msg;
}

function getTotal2() {
    var total=0;
    var total1 = 0;
    var total2 = 0;
    var total3 = 0;
    var total4 = 0;
    var count=0;
    $("input:radio:checked").each(function() {
    // Iterate through all checked radio buttons
    if (count < 6) {
        total1 = total1 + parseInt(this.value);
        document.getElementById('id_end_design_value').innerHTML = total1;
        count = count + 1;
    }
    else if (count >= 6 && count < 12) {
        total2 = total2 + parseInt(this.value);
        document.getElementById('id_end_instructor_value').innerHTML = total2;
        count = count + 1;
    }
    else if(count >= 12 && count < 16) {
        total3 = total3 + parseInt(this.value);
        document.getElementById('id_end_tutorial_value').innerHTML = total3;
        count = count + 1;
    }
    else {
        total4 = total4 + parseInt(this.value);
        document.getElementById('id_end_exam_value').innerHTML = total4;
        count = count + 1;
    }

});

    document.getElementById('id_end_design_value').value = total1;
    document.getElementById('id_end_instructor_value').value = total2;
    document.getElementById('id_end_tutorial_value').value = total3;
    document.getElementById('id_end_exam_value').value = total4;



    var msg= "Some comments about the course:";
    var inputElements = document.getElementsByName('poll13a');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].checked){
           msg = msg.concat("\n->".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll13b');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].checked){
           msg = msg.concat("\n->".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll13tb');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('topic_suggestion');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('implementation_change');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->Changes to the implementation: ".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('more_emperical_approach');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->Topics that need a more empirical approach: ".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll21a');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].checked){
           msg = msg.concat("\n->Instructor was not clear due to: ".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll21atb');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->Instructor was not clear due to: ".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll31a');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].checked){
           msg = msg.concat("\n->Tutorials were not helpful because: ".concat(inputElements[i].value));
      }
    }
    inputElements = document.getElementsByName('poll31atb');
    for(var i=0; inputElements[i]; ++i){
      if(inputElements[i].value!=""){
           msg = msg.concat("\n->Tutorials were not helpful because: ".concat(inputElements[i].value));
      }
    }
    msg = msg.concat("\nPlease take measures to improve on these.");

    document.getElementById('id_post').value = msg;
}

