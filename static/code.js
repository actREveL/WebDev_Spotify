

// Event-Handler für Veränderung im Länder-Select
$('#region-select').change(function (value) {
  var selected = $('#region-select').val();

  // Daten eines bestimmten Landes laden
  loadTable(selected)
});


// Hilfsfunktion, lädet Daten für eine bestimmte Region
function loadTable(region) {
  $.get('/api?region=' + region, function (result) {
    let html = '';
    for (let row of result) {
      let row_html = `
          <tr>
            <th scope="row">${row['Rank']}</th>
            <td>${row['Title']}</td>
            <td>${row['Artist']}</td>
            <td>${row['Date']}</td>
            <td>${row['Region']}</td>
            <td>${row['Streams']}</td>
            <td><a href="${row['URL']}">Link</a></td>
          </tr>
          `

      html = html + row_html;
    }

    $('#table-body').html(html);
  })
}
// function countries() {
//   for (row in result) {
//     let row_region = $(row['Region'])
//   }
//   console.log(row_region)
// }

// countries()



// prevent changing weeks and months
// var weekOptions = {
//   "changeMonth": false, "changeYear": false, "stepMonths": 0, beforeShowDay: function (date) {
//     return [date.getDay() == 1, ''];
//   }
// };

// $(function () {
//   $(".week").datepicker("option", weekOptions);
// });

// Datepicker

loadTable('Switzerland')