$("#cancelbtn").on("click", function () {
  location.reload();
});

// qnty to Amont function
var Qunty = $("#prductpriceid").val();
    $("#txtQuantity").on("input", function () {
          
        if (parseInt($("#txtQuantity").val()) >parseInt( $("#grnqtyedit").val())) {
          $(this).val(parseInt( $("#grnqtyedit").val()));
        }
        var quan_tity = $("#txtQuantity").val();
        var amt = Qunty * quan_tity;
        $("#txtAmount").val(amt);
        console.log(amt)
    });

function purchsefunction() {
    
  supplier_id = $("#ddlSupplierName").val();
  date_id = $("#txtdDate").val();
  quantity_id = $("#txtQuantity").val();
  product_id = $("#ddlItemName").val();
  Amount_id = $("#txtAmount").val();
  console.log(supplier_id, date_id, quantity_id, product_id, Amount_id);

  $.ajax({
    url: "{% url 'temprary_purchase' %}",
    type: "POST",
    data: {
      supplier: supplier_id,
      date: date_id,
      quantity: quantity_id,
      product: product_id,
      Amount: Amount_id,
      csrfmiddlewaretoken: "{{ csrf_token }}",
    },
    dataType: "json",

    success: function (data) {
      console.log(data.purchase_bill.length);
      console.log(data);

      $("#tbodyRow").empty();
      if (data.purchase_bill.length === 0) {
        var noDataMessage =
          '<p colspan="6"  style="position: absolute;right: 50%;top: 50%;">No data found</p>';
        $("#trNoRecord").append(noDataMessage);
        $("#txtTaxableAmount").val(0.0);
      } else {
        $.each(data.purchase_bill, function (index, value) {
          var delete_url = "temprypurchse_delete(" + value.id + ")";
          var edit_url = "edit_tempraypurchase(" + value.id + ")";

          var row =
            "<tr>" +
            "<td>" +
            value.date +
            "</td>" +
            "<td>" +
            value.product_name +
            "</td>" +
            "<td>" +
            value.supplier_name +
            "</td>" +
            "<td>" +
            value.quantity +
            "</td>" +
            "<td>" +
            value.amount +
            "</td>" +
            "<td>" +
            '<a onclick="' +
            delete_url +
            '">' +
            '<i class="fa-solid fa-trash fa-fade fa-xl"></i>' +
            "</a>" +
            "&nbsp;  &nbsp;" +
            '<a onclick="' +
            edit_url +
            '">' +
            ' <i class="fa-sharp fa-solid fa-pen-to-square fa-fade fa-xl"></i>' +
            " </a>" +
            "&nbsp;  &nbsp;" +
            "</td></tr>";

          $("#tbodyRow").append(row);
          $("#txtTaxableAmount").val(value.amount);
        });

        $("#ddlSupplierName").val("");
        $("#txtdDate").val();
        $("#txtQuantity").val("");
        $("#ddlItemName").val("");
        $("#txtAmount").val("");
      }
      $("#message_show").show();
      setTimeout(function () {
        $("#message_show").hide();
      }, 3000);
    },
  });
}

// -----------tempurchase delete
function temprypurchse_delete(id) {
  $.ajax({
    url: "{% url 'Delete_tempurchase' %}",
    type: "POST",
    data: {
      billid: id,

      csrfmiddlewaretoken: "{{ csrf_token }}",
    },
    dataType: "json",
    success: function (data) {
      console.log(data.purchase_bill.length);
      console.log(data);
      $("#trNoRecord").show();
      $("#tbodyRow").empty();
      if (data.purchase_bill.length === 0) {
        var noDataMessage =
          '<p colspan="6"  style="position: absolute;right: 50%;top: 50%;">No data found</p>';
        $("#trNoRecord").append(noDataMessage);
        $("#txtTaxableAmount").val(0.0);
      } else {
        $.each(data.purchase_bill, function (index, value) {
          var delete_url = "temprypurchse_delete(" + value.id + ")";
          var edit_url = "edit_tempraypurchase(" + value.id + ")";

          var row =
            "<tr>" +
            "<td>" +
            value.date +
            "</td>" +
            "<td>" +
            value.product_name +
            "</td>" +
            "<td>" +
            value.supplier_name +
            "</td>" +
            "<td>" +
            value.quantity +
            "</td>" +
            "<td>" +
            value.amount +
            "</td>" +
            "<td>" +
            '<a onclick="' +
            delete_url +
            '">' +
            '<i class="fa-solid fa-trash fa-fade fa-xl"></i>' +
            "</a>" +
            "&nbsp;  &nbsp;" +
            '<a onclick="' +
            edit_url +
            '">' +
            ' <i class="fa-sharp fa-solid fa-pen-to-square fa-fade fa-xl"></i>' +
            " </a>" +
            "&nbsp;  &nbsp;" +
            "</td></tr>";

          $("#tbodyRow").append(row);
        });

        $("#ddlSupplierName").val("");
        $("#txtdDate").val();
        $("#txtQuantity").val("");
        $("#ddlItemName").val("");
        $("#txtAmount").val("");
      }
      $("#deletedmessage_show").show();
      setTimeout(function () {
        $("#deletedmessage_show").hide();
      }, 3000);
    },
  });
}

function updatecancel_Function() {
  $("#transporterid").val("");
  $("#amountid").val("");
  $("#shipping_typeid").val("");
  $("#customerid").val("");
}
//   tempry purchase value get
function edit_tempraypurchase(id) {
  $.ajax({
    url: "{% url 'Edit_temprypurchase' %}",
    data: {
      purchaseid: id,
      csrfmiddlewaretoken: "{{ csrf_token }}",
    },
    dataType: "json",
    success: function (data) {
      console.log(data);

      $("#ddlSupplierName")
        .find('option[value="' + data.supplier + '"]')
        .prop("selected", true);

      $("#txtdDate").val(data.date);

      $("#txtAmount").val(data.amount);

      $("#txtQuantity")
        .find('option[value="' + data.quantity + '"]')
        .prop("selected", true);

      $("#ddlItemName")
        .find('option[value="' + data.product + '"]')
        .prop("selected", true);

      $("#btnupdate").attr("onclick", "temprypurchase_update(" + data.id + ")");
      $("#btnAdd").hide();
      $("#btnupdate").show();
    },
  });
}
// update temprray purchase function
function temprypurchase_update(id) {
  supplier_id = $("#ddlSupplierName").val();
  date_id = $("#txtdDate").val();
  quantity_id = $("#txtQuantity").val();
  product_id = $("#ddlItemName").val();
  Amount_id = $("#txtAmount").val();
  console.log(supplier_id, date_id, quantity_id, product_id, Amount_id);

  $.ajax({
    url: "{% url 'temprary_purchase_update' %}",
    type: "POST",
    data: {
      purchseid: id,
      supplier: supplier_id,
      date: date_id,
      quantity: quantity_id,
      product: product_id,
      Amount: Amount_id,
      csrfmiddlewaretoken: "{{ csrf_token }}",
    },
    dataType: "json",

    success: function (data) {
      console.log(data.purchase_bill.length);
      console.log(data);

      $("#tbodyRow").empty();
      if (data.purchase_bill.length === 0) {
        var noDataMessage =
          '<p colspan="6"  style="position: absolute;right: 50%;top: 50%;">No data found</p>';
        $("#trNoRecord").append(noDataMessage);
        $("#txtTaxableAmount").val(0.0);
      } else {
        $.each(data.purchase_bill, function (index, value) {
          var delete_url = "temprypurchse_delete(" + value.id + ")";
          var edit_url = "edit_tempraypurchase(" + value.id + ")";

          var row =
            "<tr>" +
            "<td>" +
            value.date +
            "</td>" +
            "<td>" +
            value.product_name +
            "</td>" +
            "<td>" +
            value.supplier_name +
            "</td>" +
            "<td>" +
            value.quantity +
            "</td>" +
            "<td>" +
            value.amount +
            "</td>" +
            "<td>" +
            '<a onclick="' +
            delete_url +
            '">' +
            '<i class="fa-solid fa-trash fa-fade fa-xl"></i>' +
            "</a>" +
            "&nbsp;  &nbsp;" +
            '<a onclick="' +
            edit_url +
            '">' +
            ' <i class="fa-sharp fa-solid fa-pen-to-square fa-fade fa-xl"></i>' +
            " </a>" +
            "&nbsp;  &nbsp;" +
            "</td></tr>";

          $("#tbodyRow").append(row);
          $("#txtTaxableAmount").val(value.amount);
        });

        $("#ddlSupplierName").val("");
        $("#txtdDate").val();
        $("#txtQuantity").val("");
        $("#ddlItemName").val("");
        $("#txtAmount").val("");

        $("#btnAdd").show();
        $("#btnupdate").hide();
      }
      $("#updatedmessage_show").show();
      setTimeout(function () {
        $("#updatedmessage_show").hide();
      }, 3000);
    },
  });
}
// ---------------------
function validateform() {
   
  var ddlSupplierName = document.getElementById("ddlSupplierName").value.trim();
  var ddlItemName = document.getElementById("ddlItemName").value.trim();
  var txtQuantity = document.getElementById("txtQuantity").value.trim();
  var txtAmount = document.getElementById("txtAmount").value.trim();
  
  var isValid = true;
  if (ddlSupplierName === "") {
    document.getElementById("ddlSupplierName").style.border = "1px solid red";
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