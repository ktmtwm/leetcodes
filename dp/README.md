

Fibonacci
fn = fn-1 + fn-2

->

with cacheing
    init
        fn = unknown
    if(unknown) fn = fn-1 + fn-2

->

DP
    from small to big

    f(n){
        long back2 = 0, back1 = 1;
	long next;
	if(n==0) return 0;
	for(i=2; i<n; i++){
	    next = back1 + back2;
	    back2 = back1;
	    back1 = next;
	}
	return (back2 + back1);
    
    }



