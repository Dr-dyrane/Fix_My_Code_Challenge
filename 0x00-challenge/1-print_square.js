#!/usr/bin/node
/*
Print Square

This script prints a square with the character '#'
based on the provided size argument.

Requirements:
- Node.js

Usage:
  ./1-print_square.js <size>

Example:
  ./1-print_square.js 4
  Output:
  ####
  ####
  ####
  ####

Author:
- Alexander Udeogaranya
*/

if (process.argv.length <= 2) {
  process.stderr.write("Missing argument\n");
  process.stderr.write("Usage: ./1-print_square.js <size>\n");
  process.stderr.write("Example: ./1-print_square.js 8\n");
  process.exit(1);
}

const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  process.stderr.write(
    "Invalid size argument. Please provide a valid integer.\n"
  );
  process.exit(1);
}

/**
 * Prints a square with the character '#' based on the provided size.
 *
 * @param {number} size - The size of the square.
 * @returns {void}
 */
function printSquare(size) {
  for (let i = 0; i < size; i++) {
    let line = "";
    for (let j = 0; j < size; j++) {
      line += "#";
    }
    console.log(line);
  }
}

/* Call the printSquare function with the provided size */
printSquare(size);
