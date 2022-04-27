function addHideClass(tagElement, className) {
  var select = tagElement;
  var value = select.options[select.selectedIndex].value;

  if (value != "hide-value") {
    $("." + className).addClass("hide-individual-options")
  } else {
    $("." + className).removeClass("hide-individual-options")
  }
}


function addDots(input) {
  var value = input.value;

  if (value.includes(",") || value == 0) {
    return;
  }

  value = value.split(".").join("")
  var reversedValueArray = [];
  var numCount = 0;

  while (value > 0) {
    reversedValueArray.push(value % 10);
    value = Math.floor(value / 10);
    numCount++;
    if (numCount % 3 === 0 && numCount != 0) {
      reversedValueArray.push(".");
    }
  }

  var valueArray = reversedValueArray.reverse();

  if (valueArray[0] === ".") {
    valueArray.shift();
  }

  var output = valueArray.join("");
  input.value = output;
}
