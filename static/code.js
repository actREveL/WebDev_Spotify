// Default-Werte
let regionSelected = 'Switzerland'
let dateSelected = '2017-01-02'
loadTable()

// Event-Handler für Veränderung im Länder-Select
$('#region-selected').change(function () {
  regionSelected = $('#region-selected').val();

  // Daten eines bestimmten Datums laden
  loadTable()
});

// Datepicker
$(function date() {
  $("#datepicker").datepicker({
    dateFormat: 'yy-mm-dd',
    minDate: '2017-01-01',
    maxDate: '2021-12-31',
    firstDay: 1,
    changeMonth: true,
    changeYear: true,
    beforeShowDay: function (date) { return [date.getDay() == 1, ""] }
  });
});

// Event-Handler für Veränderung im Datum-Select
$('#datepicker').change(function () {
  dateSelected = $('#datepicker').val();

  // Daten eines bestimmten Datums laden
  loadTable()
})

// Hilfsfunktion, lädt Daten für eine bestimmte Region -> Bsp.: http://127.0.0.1:5000/api?region=Argentina&date=2017-01-02
function loadTable() {
  $.get('/api?region=' + regionSelected + '&date=' + dateSelected, function (result) {
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

// Länderliste
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