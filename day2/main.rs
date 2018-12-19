const INPUT: &'static str = include_str!("./input.txt");
use std::collections::{HashMap};

fn main() {
  let mut count_twice = 0;
  let mut count_thrice = 0;

  let mut counter = HashMap::new();
  
  for line in INPUT.lines() {

    for c in line.chars() {
      let count = counter.entry(c).or_insert(0);
      *count += 1;
    }

    for key in counter.keys() {
      if counter.get(key) == Some(&2) {
        count_twice += 1;
        break;
      }
    }

    for key in counter.keys() {
      if counter.get(key) == Some(&3) {
        count_thrice += 1;
        break;
      }
    }
    
    counter.clear();  
  }

  println!("twice: {}", count_twice * count_thrice);
}