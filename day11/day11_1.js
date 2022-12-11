monkeys = {
  0:
  {
    items: [57, 58],
    Operation: old => old * 19,
    Test: val => val % 7 == 0 ? 2 : 3
  },

  1:
  {
    items: [66, 52, 59, 79, 94, 73],
    Operation: old => old + 1,
    Test: val => val % 19 == 0 ? 4 : 6
  },

  2:
  {
    items: [80],
    Operation: old => old + 6,
    Test: val => val % 5 == 0 ? 7 : 5
  },

  3:
  {
    items: [82, 81, 68, 66, 71, 83, 75, 97],
    Operation: old => old + 5,
    Test: val => val % 11 == 0 ? 5 : 2
  },

  4:
  {
    items: [55, 52, 67, 70, 69, 94, 90],
    Operation: old => old * old,
    Test: val => val % 17 == 0 ? 0 : 3
  },

  5:
  {
    items: [69, 85, 89, 91],
    Operation: old => old + 7,
    Test: val => val % 13 == 0 ? 1 : 7
  },

  6:
  {
    items: [75, 53, 73, 52, 75],
    Operation: old => old * 7,
    Test: val => val % 2 == 0 ? 0 : 4
  },

  7:
  {
    items: [94, 60, 79],
    Operation: old => old + 2,
    Test: val => val % 3 == 0 ? 1 : 6
  }
}

monkeyCounter = {
  0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0
}

function doMonkeyBusiness(){
  for(let i=0;i<8;i++){
    while(monkeys[i].items.length){
      const currItem = monkeys[i].items.shift()
      const newWorry = monkeys[i].Operation(currItem)
      const boredWorryLevel = Math.trunc(newWorry/3);
      const toMonkey = monkeys[i].Test(boredWorryLevel)
      monkeys[toMonkey].items.push(boredWorryLevel)
      monkeyCounter[i]++
    }
  }
}

for(let round =0; round < 20; round++){
  doMonkeyBusiness()
  console.log(round)
}

console.log(monkeyCounter)
top = Object.values(monkeyCounter).sort((a,b)=> b-a).slice(0,2)
console.log(top[0]*top[1])