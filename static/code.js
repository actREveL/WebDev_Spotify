
// braucht man evtl. für Default-Werte:
// var region = 'Switzerland';
// var date = '2017-01-01';

// Event-Handler für Veränderung im Länder-Select
$('#region-selected').change(function () {
  var selected = $('#region-selected').val();

  // Daten eines bestimmten Landes laden
  loadTable(selected, '2017-01-02')
});


// Datepicker -> muss noch mit Datenbank verbunden werden + change Event o.ä.
$(function date() {
  $("#datepicker").datepicker({
    dateFormat: 'yy-mm-dd',
    minDate: '2017-01-01',
    maxDate: '2021-12-31'
  });
});


// Hilfsfunktion, lädet Daten für eine bestimmte Region -> http://127.0.0.1:5000/api?region=Argentina&date=2017-01-02
function loadTable(region, dateSelected) {
  $.get('/api?region=' + region + '&date=' + dateSelected, function (result) {
    let html = '';
    for (let row of result) {
      let d = new Date(row['date'])
      let dStr = `${d.getDate()}.${d.getMonth() + 1}.${d.getFullYear()}`
      let row_html = `
          <tr>
            <th scope="row">${row['rank']}</th>
            <td>${row['title']}</td>
            <td>${row['artist']}</td>
            <td>${dStr}</td>
            <td>${row['region']}</td>
            <td>${row['streams']}</td>
            <td><a href="${row['url']}">Link</a></td>
          </tr>
          `

      html = html + row_html;
    }

    $('#table-body').html(html);
  })
}

// Liste für Länder (Ohne Duplikate) soll erstellt werden, wodruch im HTML File nachher diese Daten im Dropdown 
// angezeigt werden können etc.

function countries() {
  $.get('/apicountry', function (country) {
    let countrylist = '<option selected>Select country ...</option>'
    for (row of country) {
      let row_country = `<option>${row}</option>`
      countrylist = countrylist + row_country
    }
    $('#region-selected').html(countrylist)
  })
}

countries()

// loadTable('Argentina', '2017-01-02')