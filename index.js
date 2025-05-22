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
}


function get_prime_numbers(n)
{
  const primes = [];
  for (let num = 2; num <= n; num++)
    { // Перебираємо всі числа від 2 до n
    let isPrime = true;
    for (let i = 2; i <= Math.sqrt(num); i++){
      if (num % i === 0){
        isPrime = false;
        break;
      }
    }
    if (isPrime){ // Якщо число простоб додаємо до списку
      primes.push(num);
    }
  }
  return primes;  // Повертаємо список простих чисел
}

// Приклад використання
let n = 30;
console.log("Прості числа від 0 до" + n + ":", get_prime_numbers(n));


/*function squares_sum(l)
{
  let t = 0; // Змінна для накопичення суми
  for (let x )
}*/


function generateTable() { 
  const tbl = document.createElement("table");
  tbl.classList.add('battle-field');
  const tblBody = document.createElement("tbody");
  
  const columnLetters = "ABCDEFGHIJ";

  for (let i = 0; i < 11; i++) {
    const row = document.createElement("tr");
    if (i === 0) {
      row.classList.add('column-letters');
    }
    
    for (let j = 0; j < 11; j++) {
      const cell = document.createElement("td");

      if (i === 0 && j === 0) {
        // Верхній лівий кут — порожній
        cell.appendChild(document.createTextNode(""));
      } else if (i === 0) {
        // Верхній рядок — літери A-J
        cell.appendChild(document.createTextNode(columnLetters[j - 1]));
        cell.style.fontWeight = "bold";
        cell.style.textAlign = "center";
      } else if (j === 0) {
        // Перший стовпчик — числа 1-10
        cell.appendChild(document.createTextNode(i));
        cell.style.fontWeight = "bold";
        cell.style.textAlign = "center";
      } else {
        // Основні клітинки — можеш залишити пустими або щось писати
        // const cellText = document.createTextNode(`(${i}, ${columnLetters[j - 1]})`);
        // cell.appendChild(cellText);
      }

      if (i > 0 && j > 0) {
        cell.classList.add('ship-cell');
      }

      row.appendChild(cell);
    }

    tblBody.appendChild(row);
  }

  tbl.appendChild(tblBody);
  tbl.style.border = "1px solid black";
  tbl.style.borderCollapse = "collapse";

  document.body.appendChild(tbl);
}