/** Compute the value of an expression in Reverse Polish Notation. Supported operators are "+", "­", "*" and "/".
* Reverse Polish is a postfix mathematical notation in which each operator immediately follows its operands.
* Each operand may be a number or another expression.
* For example, 3 + 4 in Reverse Polish is 3 4 + and 2 * (4 + 1) would be written as 4 1 + 2 * or 2 4 1 + *
*
* @param ops a sequence of numbers and operators, in Reverse Polish Notation
* @return the result of the computation
* @throws IllegalArgumentException ops don't represent a well­formed RPN expression
* @throws ArithmeticException the computation generates an arithmetic error, such as dividing by zero
*
* Some sample ops and their results:
* ["4", "1", "+", "2.5", "*"] ­> ((4 + 1) * 2.5) ­> 12.5
* ["5", "80", "40", "/", "+"] ­> (5 + (80 / 40)) ­> 7
*/
let rpn = a => {
    let operands = new Array();
    res = 0;
    a.forEach(e => {
        // invalid if there's an operator without two operands on stack
        if (e === "+"){
            operands.push(operands.pop() + operands.pop());
        } else if (e === "-"){
            operands.push(-operands.pop() + operands.pop());
        } else if (e === "*"){
            operands.push(operands.pop() * operands.pop());
        } else if (e === "/"){
            numerator = operands.pop();
            // div by zero case
            operands.push(numerator / operands.pop());
        } else if (e == "!") {
            operands.push(Math.factorial(operands.pop()));
        }
        // invalid if there's an operand left on the stack at the end
    });
}

// let rpnr = (a, i) => {

// }