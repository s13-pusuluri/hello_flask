
      var ctx = document.getElementById('myChart').getContext('2d');
      var myChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Accu-Chek Aviva Test Strips', 'Himalaya Diabecon Blood Sugar Tablets', 'Ensure Diabetes Care Powder', 'CVS Health Stomach Relief','Gaviscon Chewable Antacid Tablets Original','Pepto Bismol Travel Size- 3.4 fl oz','Voltaren Arthritis pain- 3.53 oz','Volini Pain Relief Spray','Himalaya Shigru Bone & joint'],
          datasets: [{
            label: 'Number of Products',
            data: [123, 325, 130, 520,234,435,155,256,638],
            backgroundColor: [
              'rgba(255, 99, 132, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(255, 206, 86, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(622, 123, 11, 0.2)',
              'rgba(123, 788, 124, 0.2)',
              'rgba(32, 234, 345, 0.2)',
              'rgba(345, 23, 145, 0.2)',
              'rgba(298, 1, 534, 0.2)'
            ],
            borderColor: [
              'rgba(255, 99, 132, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(255, 206, 86, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(622, 123, 11, 1)',
              'rgba(123, 788, 124, 1)',
              'rgba(32, 234, 345, 1)',
              'rgba(345, 23, 145, 0.2)',
              'rgba(298, 1, 534, 0.2)'

            ],
            borderWidth: 1
          }]
        },
        options: {
          scales: {
            yAxes: [{
              ticks: {
                beginAtZero: true
              }
            }]
          }
        }
      });