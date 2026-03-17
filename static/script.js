// const table = document.querySelector('#measurements-table');

// // check if the table exists before trying to paginate it
// if (table) {
//   const rowsPerPage = 20;
//   const rows = document.querySelectorAll('#measurements-table tbody tr');
//   const pageCount = Math.ceil(rows.length / rowsPerPage);

//   const pageInfo = document.getElementById('pageInfo');
//   const prevBtn = document.getElementById('prevBtn');
//   const nextBtn = document.getElementById('nextBtn');
//   let currentPage = 1;

//   function showPage (page) {
//     rows.forEach((row, index) => {
//       const start = (page - 1) * rowsPerPage;
//       const end = start + rowsPerPage;

//       if (index >= start && index < end) {
//         row.style.display = '';
//       } else {
//         row.style.display = 'none';
//       }
//     });
//     pageInfo.innerText = currentPage + ' / ' + pageCount;

//     prevBtn.disabled = (currentPage === 1);
//     nextBtn.disabled = (currentPage === pageCount);
//   }

//   prevBtn.onclick = function () {
//     if (currentPage > 1) {
//       currentPage--;
//       showPage(currentPage);
//     }
//   };

//   nextBtn.onclick = function () {
//     if (currentPage < pageCount) {
//       currentPage++;
//       showPage(currentPage);
//     }
//   };

//   showPage(currentPage);
// }

// Fetch statistics and update the front page
function updateStatistics () {
  // Fetch statistics from pythonanywhere
  const xhr = new XMLHttpRequest();

  xhr.open('GET', window.location.origin + '/api/statistics', true);

  xhr.onload = function () {
    if (xhr.status === 200) {
      const data = JSON.parse(xhr.responseText);
      // Check if data contains the expected properties
      if (!data.latest) return;
      if (!data.min_tvoc || !data.max_tvoc) return;

      /* Latest measurement */
      document.getElementById('lastTvocValue').innerText =
                data.latest.TVOC;

      document.getElementById('lastEco2Value').innerText =
                data.latest.eCO2;

      document.getElementById('lastTimestamp').innerText =
                new Date(data.latest.timestamp).toLocaleString();

      /* Minimum values */
      document.getElementById('minimumTvocValue').innerText =
                data.min_tvoc.TVOC;

      document.getElementById('minimumTvocTimestamp').innerText =
                new Date(data.min_tvoc.timestamp).toLocaleString();

      document.getElementById('minimumEco2Value').innerText =
                data.min_eco2.eCO2;

      document.getElementById('minimumEco2Timestamp').innerText =
                new Date(data.min_eco2.timestamp).toLocaleString();

      /* Maximum values */
      document.getElementById('maximumTvocValue').innerText =
                data.max_tvoc.TVOC;

      document.getElementById('maximumTvocTimestamp').innerText =
                new Date(data.max_tvoc.timestamp).toLocaleString();

      document.getElementById('maximumEco2Value').innerText =
                data.max_eco2.eCO2;

      document.getElementById('maximumEco2Timestamp').innerText =
                new Date(data.max_eco2.timestamp).toLocaleString();
    }
  };

  xhr.onerror = function () {
    console.error('Error fetching statistics');
  };

  xhr.send();
}

// Update front page statistics every minute
updateStatistics();
setInterval(updateStatistics, 60000);
