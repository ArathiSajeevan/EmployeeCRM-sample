// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = 'Nunito', '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#858796';

// Pie Chart Example
var ctx = document.getElementById("myPieChart");
var a=document.getElementById("income").innerHTML;
var b=document.getElementById("profit").innerHTML;
var c=document.getElementById("expense").innerHTML;

if (a<=0){a=0;}
if (b<=0){b=0;}
if (c<=0){c=0;}

console.log(a)
console.log(b)
console.log(c)

var myPieChart = new Chart(ctx, {
  type: 'doughnut',
  data: {
    labels: ["Enquiry", "Orders", "Failed"],
    datasets: [{
      data: [a, b, c,],
      backgroundColor: ['#5bc0de', '#5cb85c', '#d9534f'],
      hoverBackgroundColor: ['#408599', '#326e32', '#9e3c39'],
      hoverBorderColor: "rgba(234, 236, 244, 1)",
    }],
  },
  options: {
    maintainAspectRatio: false,
    tooltips: {
      backgroundColor: "rgb(255,255,255)",
      bodyFontColor: "#858796",
      borderColor: '#dddfeb',
      borderWidth: 1,
      xPadding: 15,
      yPadding: 15,
      displayColors: false,
      caretPadding: 10,
    },
    legend: {
      display: false
    },
    cutoutPercentage: 80,
  },
});
