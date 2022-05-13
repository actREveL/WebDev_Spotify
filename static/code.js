
$.get('/api', function (result) {
  let html = '';
  for (let row of result) {
    console.log(row)
    let row_html = `
        <tr>
          <th scope="row">${row['Rank']}</th>
          <td>${row['Title']}</td>
          <td>${row['Artist']}</td>
          <td>${row['Date']}</td>
          <td>${row['Region']}</td>
          <td>${row['Streams']}</td>
          <td>${row['URL']}</td>
        </tr>
        `

    html = html + row_html;
  }

  $('#table-body').html(html);
})