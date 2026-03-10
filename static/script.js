const rowsPerPage = 20;
const rows = document.querySelectorAll('#measurements-table tbody tr');
const pageCount = Math.ceil(rows.length / rowsPerPage);

const pageInfo = document.getElementById('pageInfo');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
let currentPage = 1;

function showPage (page) {
  rows.forEach((row, index) => {
    const start = (page - 1) * rowsPerPage;
    const end = start + rowsPerPage;

    if (index >= start && index < end) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
  pageInfo.innerText = currentPage + ' / ' + pageCount;

  prevBtn.disabled = (currentPage === 1);
  nextBtn.disabled = (currentPage === pageCount);
  prevBtn.enabled = (currentPage !== 1);
  nextBtn.enabled = (currentPage !== pageCount);
}

prevBtn.onclick = function () {
  if (currentPage > 1) {
    currentPage--;
    showPage(currentPage);
  }
};

nextBtn.onclick = function () {
  if (currentPage < pageCount) {
    currentPage++;
    showPage(currentPage);
  }
};

showPage(currentPage);
