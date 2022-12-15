document.querySelector(".add").addEventListener("click", e => {
    document.querySelector(".modal-wrapper").style.display = "flex";
})
document.querySelector(".close").addEventListener("click", e => {
    document.querySelector(".modal-wrapper").style.display = "none";
})

async function getSpendings(){
    let res = await fetch("../spendings/");
    let result = await res.json();
    return JSON.parse(result);
}


getSpendings().then(result => {
    let labels = result.map(transaction => transaction.category);
    labels = labels.filter((item, pos) => labels.indexOf(item) == pos);
    let dataset = [];
    result.forEach(transaction => {
      if(dataset[labels.indexOf(transaction.category)]){
        dataset[labels.indexOf(transaction.category)] += transaction.total;
      }
      else{
        dataset[labels.indexOf(transaction.category)] = transaction.total;
      }
    })
    const data = {
        labels,
        datasets: [
          {
            data : dataset
          }
        ]
    };
    const ctx = document.getElementById('spendings-chart');
    new Chart(ctx, {
      type: 'doughnut',
      data: data,
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Траты по категориям',
            color: "#fff"
          },
          labels: {
            color: "#fff",
            fontSize: 18
          }
        }
      },
    });
})

async function getIncome(){
  let res = await fetch("../income/");
  let result = await res.json();
  return JSON.parse(result);
}


getIncome().then(result => {
  let labels = result.map(transaction => transaction.category);
    labels = labels.filter((item, pos) => labels.indexOf(item) == pos);
    let dataset = [];
    result.forEach(transaction => {
      if(dataset[labels.indexOf(transaction.category)]){
        dataset[labels.indexOf(transaction.category)] += transaction.total;
      }
      else{
        dataset[labels.indexOf(transaction.category)] = transaction.total;
      }
    })
    const data = {
        labels,
        datasets: [
          {
            data : dataset
          }
        ]
    };
    const ctx = document.getElementById('income-chart');
    new Chart(ctx, {
      type: 'doughnut',
      data: data,
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
          title: {
            display: true,
            text: 'Траты по категориям',
            color: "#fff"
          },
          labels: {
            color: "#fff",
            fontSize: 18
          }
        }
      },
    });
})