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
};
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

    var a1 = document.getElementsByName('poll11');
    var a2 = document.getElementsByName('poll12');
    var a3 = document.getElementsByName('poll13');
    var a4 = document.getElementsByName('poll14');
    var a5 = document.getElementsByName('poll15');
    var a6 = document.getElementsByName('poll16');
    var b1 = document.getElementsByName('poll21');
    var b2 = document.getElementsByName('poll22');
    var b3 = document.getElementsByName('poll23');
    var b4 = document.getElementsByName('poll24');
    var b5 = document.getElementsByName('poll25');
    var b6 = document.getElementsByName('poll26');
    var c1 = document.getElementsByName('poll31');
    var c2 = document.getElementsByName('poll32');
    var c3 = document.getElementsByName('poll33');
    var c4 = document.getElementsByName('poll34');
    var d1 = document.getElementsByName('poll41');
    var d2 = document.getElementsByName('poll42');
    var d3 = document.getElementsByName('poll43');


    for(var i=0; a1[i]; ++i){
      if(a1[i].checked){
           total1 = total1 + 1;
      }
    }

    for(var i=0; a2[i]; ++i){
      if(a2[i].checked){
           total1 = total1 + 1;
      }
    }

    for(var i=0; a3[i]; ++i){
      if(a3[i].checked){
           total1 = total1 + 1;
      }
    }

    for(var i=0; a4[i]; ++i){
      if(a4[i].checked){
           total1 = total1 + 1;
      }
    }

    for(var i=0; a5[i]; ++i){
      if(a5[i].checked){
           total1 = total1 + 1;
      }
    }

    for(var i=0; a6[i]; ++i){
      if(a6[i].checked){
           total1 = total1 + 1;
      }
    }

    for(var i=0; b1[i]; ++i){
      if(b1[i].checked){
           total2 = total2 + 1;
      }
    }

    for(var i=0; b2[i]; ++i){
      if(b2[i].checked){
           total2 = total2 + 1;
      }
    }

    for(var i=0; b3[i]; ++i){
      if(b3[i].checked){
           total2 = total2 + 1;
      }
    }

    for(var i=0; b4[i]; ++i){
      if(b4[i].checked){
           total2 = total2 + 1;
      }
    }

    for(var i=0; b5[i]; ++i){
      if(b5[i].checked){
           total2 = total2 + 1;
      }
    }

    for(var i=0; b6[i]; ++i){
      if(b6[i].checked){
           total2 = total2 + 1;
      }
    }

    for(var i=0; c1[i]; ++i){
      if(c1[i].checked){
           total3 = total3 + 1;
      }
    }
    for(var i=0; c2[i]; ++i){
      if(c2[i].checked){
           total3 = total3 + 1;
      }
    }
    for(var i=0; c3[i]; ++i){
      if(c3[i].checked){
           total3 = total3 + 1;
      }
    }
    for(var i=0; c4[i]; ++i){
      if(c4[i].checked){
           total3 = total3 + 1;
      }
    }

    for(var i=0; d1[i]; ++i){
      if(d1[i].checked){
           total4 = total4 + 1;
      }
    }
    for(var i=0; d2[i]; ++i){
      if(d2[i].checked){
           total4 = total4 + 1;
      }
    }
    for(var i=0; d3[i]; ++i){
      if(d3[i].checked){
           total4 = total4 + 1;
      }
    }

    // $("input:radio:checked").each(function() {
    // // Iterate through all checked radio buttons
    // if (count < 6) {
    //     total1 = total1 + parseInt(this.value);
    //     document.getElementById('id_mid_design_value').innerHTML = total1;
    //     count = count + 1;
    // }
    // else if (count >= 6 && count < 12) {
    //     total2 = total2 + parseInt(this.value);
    //     document.getElementById('id_mid_instructor_value').innerHTML = total2;
    //     count = count + 1;
    // }
    // else if(count >= 12 && count < 16) {
    //     total3 = total3 + parseInt(this.value);
    //     document.getElementById('id_mid_tutorial_value').innerHTML = total3;
    //     count = count + 1;
    // }
    // else {
    //     total4 = total4 + parseInt(this.value);
    //     document.getElementById('id_mid_exam_value').innerHTML = total4;
    //     count = count + 1;
    // }

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

