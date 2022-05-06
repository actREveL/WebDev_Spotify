
$.get('/api', function (result) {
  let html = '';
  for (let row of result) {
    let row_html = `
        <tr>
          <th scope="row">${row[0]}</th>
          <td>${row[1]}</td>
          <td>${row[2]}</td>
          <td>${row[3]}</td>
          <td>${row[4]}</td>
          <td>${row[5]}</td>
          <td>${row[6]}</td>
        </tr>
        `

    html = html + row_html;
  }

  $('#table-body').html(html);
})