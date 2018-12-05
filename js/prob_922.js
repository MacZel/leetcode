/**
 * @param {number[]} A
 * @return {number[]}
 */
const sortArrayByParityII = A => {
    let even_list = []
    let odd_list = []
    let out_list = []
    
    for (let i=0; i<A.length; i++) {
        if (A[i] % 2 == 0) {
            even_list.push(A[i])
        }
        else {
            odd_list.push(A[i])
        }
    }
    for (let i=0; i<even_list.length; i++) {
        out_list.push(even_list[i], odd_list[i])
    }
    return out_list
}