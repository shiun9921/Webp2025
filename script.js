var container = document.getElementById('container');

// 產生隨機 0 到 2 個字母
function generateRandomLetters() {
    let letters = "abcdefghijklmnopqrstuvwxyz";
    let length = Math.floor(Math.random() * 3); // 產生 0、1 或 2
    let randomStr = "";
    for (let i = 0; i < length; i++) {
        randomStr += letters[Math.floor(Math.random() * letters.length)];
    }
    return randomStr;
}

// 當網頁載入時執行
window.onload = function() {
    container.textContent = generateRandomLetters();
};

// 監聽鍵盤輸入
window.addEventListener("keyup", function(e) {
    console.log(e.key);

    if (e.key === 'Escape') {
        container.textContent = ""; // 按 ESC 清空
    } else if (e.key === 'Backspace') {
        let str = container.textContent;
        container.textContent = str.substring(0, str.length - 1); // 刪除最後一個字
    } else {
        let str = container.textContent;
        if (str.length > 0 && e.key === str[0]) {
            container.textContent = str.substring(1); // 如果輸入的字和第一個字母相同，刪除該字
        }
        // 無論如何都要增加新的隨機字元
        container.textContent += generateRandomLetters();
    }
});