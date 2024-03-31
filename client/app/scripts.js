const app = document.getElementById('root');

const container = document.createElement('div');
container.setAttribute('class', 'container');

app.appendChild(container);

var request = new XMLHttpRequest();

main();

async function main() {
  request.open('GET', 'https://8mfdub98va.execute-api.us-east-1.amazonaws.com/dev', true);
  request.onload = async function () {

    // Begin accessing JSON data here
    var data = JSON.parse(this.response);
    if (request.status >= 200 && request.status < 400) {
      data.Items.forEach(async item => {
        const card = document.createElement('div');
        card.setAttribute('class', 'card');

        const h1 = document.createElement('h1');
        h1.textContent = item.Serial;

        var when = await convert(item.date_time);

        const p = document.createElement('p');
        p.textContent = `${item.status} at ${when}`;

        container.appendChild(card);
        card.appendChild(h1);
        card.appendChild(p);

      });
    } else {
      const errorMessage = document.createElement('marquee');
      errorMessage.textContent = `Something went wrong`;
      app.appendChild(errorMessage);
    }
  }
}
request.send();
// end

function convert(unixtimestamp){
 
  // Months array
  var months_arr = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
 
  // Convert timestamp to milliseconds
  var date = new Date(unixtimestamp*1000);
 
  // Year
  var year = date.getFullYear();
 
  // Month
  var month = months_arr[date.getMonth()];
 
  // Day
  var day = date.getDate();
 
  // Hours
  var hours = date.getHours();
 
  // Minutes
  var minutes = "0" + date.getMinutes();
 
  // Seconds
  var seconds = "0" + date.getSeconds();
 
  // Display date time in MM-dd-yyyy h:m:s format
  var convdataTime = month+'-'+day+'-'+year+' '+hours + ':' + minutes.substr(-2) + ':' + seconds.substr(-2);
  return convdataTime;
  
 }