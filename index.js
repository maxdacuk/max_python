/*document.body.onload = Start;


function Start() 
{
  console.log('Start1')
  const first = 2; 
  const n = 5;    
  const step = 3; 

  const result = geo_progression_first_n_members(first, n, step);
  console.log(result); // [2, 6, 18, 54, 162]
  alert("Геометрична прогресія:\n" + result.join(', '));
}*/

/**
 * Generate the first n members of a geometric progression
 *
 * @param {int} first - the value of the first progression member
 * @param {int} n - the count of members
 * @param step - the progression step
 */
 /*
function geo_progression_first_n_members(first, n, step)
{
  const result = [];// Створюємо порожній масив для результату
    // Цикл, який повторюється n разів
  for (let i = 0; i < n; i++) {

    // Кожен новий елемент: перший * step**i
    const member = first * Math.pow(step, i);

    // Додаємо цей елемент до масиву 
    result.push(member);
  }
  return result;
}*/



const SIZE = 10;
const SHIPS = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1];

const SERVER_IP = "localhost";
const SERVER_PORT = 3000;

const playerMatrix = [];
const computerMatrix = [];

let playerField = [];
let computerField = [];

let computerHits = [];
let playerTurn = true;
let computerShips = [];
let playerShips = [];
let lastReceivedTime = 0;

/* Клас клітинки */
class Cell {
  constructor() {
    this.hasShip = false;
    this.shot = false;
  }
}

/* Створення логічного поля */
function createField() {
  const field = [];
  for (let i = 0; i < SIZE; i++) {
    const row = [];
    for (let j = 0; j < SIZE; j++) row.push(new Cell());
    field.push(row);
  }
  return field;
}

/* --- Утиліти --- */
function isInBounds(r, c) {
  return r >= 0 && r < SIZE && c >= 0 && c < SIZE;
}
function showMessage(text) {
  const box = document.getElementById("messages");
  box.textContent = text;
  if (text)
    setTimeout(() => {
      if (box.textContent === text) box.textContent = "";
    }, 2000);
}
function shuffle(arr) {
  for (let i = arr.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [arr[i], arr[j]] = [arr[j], arr[i]];
  }
  return arr;
}

/* --- Генерація таблиць --- */
function generateTables() {
  const container = document.createElement("div");
  container.style.display = "flex";
  container.style.gap = "40px";

  const playerTable = createTable("Поле гравця", playerMatrix);
  const compTable = createTable("Поле комп’ютера", computerMatrix, true);

  container.appendChild(playerTable);
  container.appendChild(compTable);
  document.body.insertBefore(container, document.getElementById("messages"));
}

function createTable(title, matrix, clickable = false) {
  const wrapper = document.createElement("div");
  const caption = document.createElement("div");
  caption.textContent = title;
  caption.style.textAlign = "center";
  caption.style.fontWeight = "bold";
  caption.style.marginBottom = "5px";
  wrapper.appendChild(caption);

  const table = document.createElement("table");
  const tbody = document.createElement("tbody");

  for (let i = 0; i < SIZE; i++) {
    const tr = document.createElement("tr");
    const rowCells = [];
    for (let j = 0; j < SIZE; j++) {
      const td = document.createElement("td");
      td.style.width = "25px";
      td.style.height = "25px";
      td.style.border = "1px solid #000";
      td.style.textAlign = "center";
      td.style.fontSize = "20px";
      td.dataset.row = i;
      td.dataset.col = j;

      if (clickable) {
        td.addEventListener("click", () => playerShoot(i, j, td));
        td.style.cursor = "pointer";
      }

      tr.appendChild(td);
      rowCells.push(td);
    }
    tbody.appendChild(tr);
    matrix.push(rowCells);
  }

  table.appendChild(tbody);
  wrapper.appendChild(table);
  return wrapper;
}

/* --- Розміщення кораблів --- */
function isAreaFree(field, row, col, size, orientation) {
  for (let r = row - 1; r <= row + (orientation === "vertical" ? size : 1); r++) {
    for (let c = col - 1; c <= col + (orientation === "horizontal" ? size : 1); c++) {
      if (isInBounds(r, c)) {
        if (field[r][c].hasShip) return false;
      }
    }
  }
  return true;
}

function placeShips(field, visibleMatrix, showShips = false) {
  const ships = [];
  for (const size of SHIPS) {
    let placed = false;
    while (!placed) {
      const orientation = Math.random() < 0.5 ? "horizontal" : "vertical";
      const row = Math.floor(Math.random() * SIZE);
      const col = Math.floor(Math.random() * SIZE);
      const coords = [];

      if (orientation === "horizontal") {
        if (col + size > SIZE) continue;
        if (!isAreaFree(field, row, col, size, orientation)) continue;

        for (let i = 0; i < size; i++) {
          field[row][col + i].hasShip = true;
          if (showShips) visibleMatrix[row][col + i].style.backgroundColor = "lightblue";
          coords.push([row, col + i]);
        }
      } else {
        if (row + size > SIZE) continue;
        if (!isAreaFree(field, row, col, size, orientation)) continue;

        for (let i = 0; i < size; i++) {
          field[row + i][col].hasShip = true;
          if (showShips) visibleMatrix[row + i][col].style.backgroundColor = "lightblue";
          coords.push([row + i, col]);
        }
      }
      ships.push(coords);
      placed = true;
    }
  }
  return ships;
}

/* --- Гравець стріляє --- */
function playerShoot(row, col, cell) {
  if (!playerTurn) return;
  const target = computerField[row][col];
  if (target.shot) return;

  // Зразу відзначаємо як оброблений, щоб не давати повторних кліків
  target.shot = true;

  // Відправка даних на сервер (асинхронно, гра не чекає відповіді)
  fetch(`http://${SERVER_IP}:${SERVER_PORT}/shoot`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ row, col })
  })
    .then(res => res.text())
    .then(msg => console.log("Від сервера:", msg))
    .catch(err => console.warn("Помилка при відправці на сервер:", err));

  // Локальна візуалізація та логіка
  if (target.hasShip) {
    cell.style.backgroundColor = "red";
    showMessage("Влучив!");
    if (checkIfSunk(computerShips, row, col, computerMatrix)) {
      showMessage("Ти потопив корабель!");
    }
    // Залишаємо хід гравця після влучання (як у класичних правилах)
  } else {
    cell.style.backgroundColor = "#ccc";
    showMessage("Промах!");
    playerTurn = false;
    // даємо час на "думку" комп'ютеру
    setTimeout(() => computerShoot(), 800 + Math.random() * 700);
  }
}

/* --- Логіка для комп’ютера --- */
function computerShoot() {
  // якщо хід вже повернувся гравцю або гра закінчена, нічого не робимо
  if (playerTurn) return;

  const target = getComputerNextTarget();
  if (!target) return;

  const [row, col] = target;
  const cell = playerMatrix[row][col];
  const enemy = playerField[row][col];

  // Відмічаємо, що вже стріляли сюди
  enemy.shot = true;

  if (enemy.hasShip) {
    cell.style.backgroundColor = "red";
    computerHits.push([row, col]);
    showMessage("Комп’ютер влучив!");
    // Перевірити потоплення
    if (checkIfSunk(playerShips, row, col, playerMatrix)) {
      showMessage("Комп’ютер потопив корабель!");
      // Очищуємо hits, бо корабель потоплено
      computerHits = [];
    }
    // після влучання комп'ютер стріляє ще раз через паузу
    setTimeout(() => computerShoot(), 800 + Math.random() * 700);
  } else {
    cell.style.backgroundColor = "#ccc";
    showMessage("Комп’ютер промахнувся!");
    playerTurn = true;
  }
}

/* --- Логіка вибору цілі комп'ютера --- */
function getComputerNextTarget() {
  if (computerHits.length >= 2) {
    const [r1, c1] = computerHits[0];
    const [r2, c2] = computerHits[1];
    const horizontal = r1 === r2;
    const vertical = c1 === c2;
    const candidates = [];

    if (horizontal) {
      const row = r1;
      const minC = Math.min(...computerHits.map(h => h[1]));
      const maxC = Math.max(...computerHits.map(h => h[1]));
      if (isInBounds(row, minC - 1) && !playerField[row][minC - 1].shot)
        candidates.push([row, minC - 1]);
      if (isInBounds(row, maxC + 1) && !playerField[row][maxC + 1].shot)
        candidates.push([row, maxC + 1]);
    } else if (vertical) {
      const col = c1;
      const minR = Math.min(...computerHits.map(h => h[0]));
      const maxR = Math.max(...computerHits.map(h => h[0]));
      if (isInBounds(minR - 1, col) && !playerField[minR - 1][col].shot)
        candidates.push([minR - 1, col]);
      if (isInBounds(maxR + 1, col) && !playerField[maxR + 1][col].shot)
        candidates.push([maxR + 1, col]);
    }

    if (candidates.length) return candidates[Math.floor(Math.random() * candidates.length)];
  }

  if (computerHits.length === 1) {
    const [row, col] = computerHits[0];
    const dirs = shuffle([
      [row - 1, col],
      [row + 1, col],
      [row, col - 1],
      [row, col + 1],
    ]);
    for (const [r, c] of dirs) {
      if (isInBounds(r, c) && !playerField[r][c].shot) return [r, c];
    }
  }

  // випадковий постріл
  const candidates = [];
  for (let r = 0; r < SIZE; r++) {
    for (let c = 0; c < SIZE; c++) {
      if (!playerField[r][c].shot) candidates.push([r, c]);
    }
  }
  if (candidates.length === 0) return null;
  return candidates[Math.floor(Math.random() * candidates.length)];
}

/* --- Перевірка потоплення --- */
function checkIfSunk(ships, row, col, matrix) {
  for (const ship of ships) {
    if (ship.some(([r, c]) => r === row && c === col)) {
      const sunk = ship.every(([r, c]) => matrix[r][c].style.backgroundColor === "red");
      return sunk;
    }
  }
  return false;
}

/* --- Старт гри --- */
function startGame() {
  fetch(`http://${SERVER_IP}:${SERVER_PORT}/shoot`, {
    method: "POST"
  })
  .then(res => res.text())
  .then(msg => console.log("Login:", msg))
  .catch(err => console.warn("Login eror:", err));

  playerField = createField();
  computerField = createField();

  generateTables();

  playerShips = placeShips(playerField, playerMatrix, true);
  computerShips = placeShips(computerField, computerMatrix, false);

  showMessage("Твій хід!");
}


function checkEnemyShot() {
  fetch(`http://${SERVER_IP}:${SERVER_PORT}/get-shot`)
    .then(res => res.json())
    .then(data => {
      if (!data) return;

      if (data.time !== lastReceivedTime) {
        lastReceivedTime = data.time;

        console.log("Отримано постріл:", data);

        enemyShoot(data.row, data.col);
      }
    })
    .catch(err => console.log(err));
}

function enemyShoot(row, col) {
  const cell = playerMatrix[row][col];
  const target = playerField[row][col];

  if (target.shot) return;

  target.shot = true;

  if (target.hasShip) {
    cell.style.backgroundColor = "red";
    showMessage("По тобі влучили!");
  } else {
    cell.style.backgroundColor = "#ccc";
    showMessage("По тобі промах!");
  }
}


startGame();

setInterval(checkEnemyShot, 1000);