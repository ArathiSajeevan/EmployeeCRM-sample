function myFunction() {
  var x = document.getElementById("APD");
  var y = document.getElementById("APD_Data");
  var day = document.getElementById("one").innerHTML;
  var month = document.getElementById("two").innerHTML;
  var year = document.getElementById("three").innerHTML;

  if (x.innerHTML === "Day") {
    x.innerHTML = "Month";
    y.innerHTML = month;
  } else if (x.innerHTML === "Month") {
    x.innerHTML = "Year";
    y.innerHTML = year;
  } else {
    x.innerHTML = "Day";
    y.innerHTML = day;
  }
}


$('.Count').each(function () {
  var $this = $(this);
  jQuery({ Counter: 0 }).animate({ Counter: $this.text() }, {
    duration: 5000,
    easing: 'linear',
    step: function () {
      $this.text(Math.ceil(this.Counter));
    }
  });
});

$('#bologna-list a').on('click', function (e) {
  e.preventDefault()
  $(this).tab('show')
});

// Delete Modal
document.addEventListener('DOMContentLoaded', () => {
    let form_confirm = document.querySelector('#form_confirm_modal')
    let buttons = document.querySelectorAll("[data-target='#deleteItemModal']");
        buttons.forEach(button => {
            button.addEventListener("click", () => {


                // extract url from calling element and replace the modals texts with it
                if (button.dataset.url) {
                    form_confirm.action = button.dataset.url;
                }

            })
        });
   let confirmModal = document.getElementById("confirmButtonModal")
    confirmModal.addEventListener('click', () => {
        form_confirm.submit();

    });
});

document.addEventListener('DOMContentLoaded', () => {
    let form_confirm1 = document.querySelector('#form_confirm_modal1')
    let buttons = document.querySelectorAll("[data-target='#deleteItemModal1']");
        buttons.forEach(button => {
            button.addEventListener("click", () => {


                // extract url from calling element and replace the modals texts with it
                if (button.dataset.url) {
                    form_confirm1.action = button.dataset.url;
                }

            })
        });
   let confirmModal1 = document.getElementById("confirmButtonModal1")
    confirmModal1.addEventListener('click', () => {
        form_confirm1.submit();

    });
});