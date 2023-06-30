document.getElementById("canslcust").addEventListener("click",function(){
    document.getElementById("customer_form").style.display="none"
    document.getElementById("logis-form").style.display="block"
 })
//  $(document).on("click","#customerButton",function(){
  
//     $("#customer_form").modal("toggle");
    
//   })

var customerButton = document.getElementById("customerButton");
var customerForm = document.getElementById("customer_form");

customerButton.addEventListener("click", function() {
  document.getElementById("logis-form").style.display="none"
  customerForm.style.display = "block";
});
// var customer_id =[] ;
// var shipping_type_id =[] ;
// var transporter_id =[] ;
// var amount_id =[] ;



// validation sscript
document.forms['customerAdd'].onsubmit = function(event){
    if (this.Customer.value.trim() === "") {
        document.getElementById("exampleInputUsername1").style.border = "1px solid red";
        document.querySelector('.firstname_error').innerHTML = "Please enter a customer name!";
        document.querySelector(".firstname_error").style.display = "block";
        event.preventDefault();
        return false;
    } else {
        document.getElementById("exampleInputUsername1").style.border = ""; 
        document.querySelector(".firstname_error").style.display = "none";
    }
    if (this.mobile.value.trim() === "") {
        document.getElementById("exampleInputUsername2").style.border = "1px solid red";
        document.querySelector('.lastname_error').innerHTML = "Please enter a customer name!";
        document.querySelector(".lastname_error").style.display = "block";
        event.preventDefault();
        return false;
    } else {
        document.getElementById("exampleInputUsername2").style.border = ""; 
        document.querySelector(".lastname_error").style.display = "none";
    }
}
document.getElementById("exampleInputUsername1").addEventListener("change", function() {
    document.getElementById("exampleInputUsername1").style.border = "";
    document.querySelector('.firstname_error').style.display = "none";
});
document.getElementById("exampleInputUsername2").addEventListener("change", function() {
    document.getElementById("exampleInputUsername2").style.border = "";
    document.querySelector('.lastname_error').style.display = "none";
});

function validateform() {
   
    var customerValue = document.getElementById("customerid").value.trim();
    var transporterValue = document.getElementById("transporterid").value.trim();
    var shippingTypeValue = document.getElementById("shipping_typeid").value.trim();
    var amountValue = document.getElementById("amountid").value.trim();
    
    var isValid = true;
    if (customerValue === "") {
      document.getElementById("customerid").style.border = "1px solid red";
      document.querySelector('.customer_error').innerHTML = "Please select a customer!";
      document.querySelector(".customer_error").style.display = "block";
      isValid = false;
    } else {
      document.getElementById("customerid").style.border = "";
      document.querySelector(".customer_error").style.display = "none";
      isValid = false;
    }
  
    if (transporterValue === "") {
      document.getElementById("transporterid").style.border = "1px solid red";
      document.querySelector('.transporter_error').innerHTML = "Please select a transporter!";
      document.querySelector(".transporter_error").style.display = "block";
      isValid = false;
    } else {
      document.getElementById("transporterid").style.border = "";
      document.querySelector(".transporter_error").style.display = "none";
      isValid = false;
    }
  
    if (shippingTypeValue === "") {
      document.getElementById("shipping_typeid").style.border = "1px solid red";
      document.querySelector('.shptype_error').innerHTML = "Please select type!";
      document.querySelector(".shptype_error").style.display = "block";
      isValid = false;
    } else {
      document.getElementById("shipping_typeid").style.border = "";
      document.querySelector(".shptype_error").style.display = "none";
      isValid = false;
    }
  
    if (amountValue === "") {
      document.getElementById("amountid").style.border = "1px solid red";
      document.querySelector('.amount_error').innerHTML = "Please enter an amount!";
      document.querySelector(".amount_error").style.display = "block";
      isValid = false;
    } else {
      document.getElementById("amountid").style.border = "";
      document.querySelector(".amount_error").style.display = "none";
      isValid = false;
    }
    
    if (!isValid) {
        tablebinding()
      return false;
    }
    
  };
  
  document.getElementById("customerid").addEventListener("change", function() {
    document.getElementById("customerid").style.border = "";
    document.querySelector('.customer_error').style.display = "none";
  });
  
  document.getElementById("transporterid").addEventListener("change", function() {
    document.getElementById("transporterid").style.border = "";
    document.querySelector('.transporter_error').style.display = "none";
  });
  
  document.getElementById("shipping_typeid").addEventListener("change", function() {
    document.getElementById("shipping_typeid").style.border = "";
    document.querySelector('.shptype_error').style.display = "none";
  });
  
  document.getElementById("amountid").addEventListener("input", function() {
    document.getElementById("amountid").style.border = "";
    document.querySelector('.amount_error').style.display = "none";
  });
  
//dhhdrrrrrrrrrrrrrrrr---------------------


// function validateForm() {
//     var customerInput = document.getElementById("customerid");
//     var customerError = document.getElementById('customer_error');
//     var customer = customerInput.value.trim();
  
//     var transporterid = document.getElementById('transporterid');
//     var transporter_error = document.getElementById('transporter_error');
//     var transporter = transporterid.value.trim();
  
//     var shipping_typeid = document.getElementById('shipping_typeid');
//     var shptype_error = document.getElementById('shptype_error');
//     var shipping_type = shipping_typeid.value;
  
//     var amountid = document.getElementById('amountid');
//     var amount_error = document.getElementById('amount_error');
//     var amount = amountid.value.trim();
  
   
//     var hasError = false;
  
//     if (customer === '') {
//         customerError.style.display = 'block';
//       hasError = true;
//     } else {
//         customerError.style.display = 'none';
//     }
  
//     if (transporter === '') {
//         transporter_error.style.display = 'block';
//       hasError = true;
//     } else {
//         transporter_error.style.display = 'none';
//     }
  
//     if (shipping_type === '') {
//         shptype_error.style.display = 'block';
//       hasError = true;
//     } else {
//       passwordError.style.display = 'none';
//     }
  
//     if (amount === '') {
//         amount_error.style.display = 'block';
//       hasError = true;
//     } else {
//         amount_error.style.display = 'none';
//     }
  
   
//     customerInput.addEventListener('change', function() {
//         customerError.style.display = customerInput.value.trim() === '' ? 'block' : 'none';
//     });
  
//     transporterid.addEventListener('change', function() {
//         transporter_error.style.display = transporterid.value.trim() === '' ? 'block' : 'none';
//     });
  
//     shipping_typeid.addEventListener('change', function() {
//         shptype_error.style.display = shipping_typeid.value === '' ? 'block' : 'none';
//     });
  
//     amountid.addEventListener('input', function() {
//         amount_error.style.display = amountid.value.trim() === '' ? 'block' : 'none';
//     });
  
   
  
//     if (hasError) {
//       return false; // Prevent form submission
//     }
  
//     // Additional custom validation logic
//     // ...
  
//     return true; // Allow form submission
//   }