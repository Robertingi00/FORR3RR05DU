class Node{
	constructor(tala){
		this.tala = tala;
		this.left = null;
		this.right = null;
	}

	insert(tala){
		if(tala < this.tala){
			if(this.left){
				this.left.insert(tala);
			}else{
				this.left = new Node(tala);
			}
		}if(tala > this.tala){
			if(this.right){
				this.right.insert(tala);
			}else{
				this.right = new Node(tala);
			}
		}
	}

	preOrderPrint(){
		console.log(this.tala);
		if(this.left){
			this.left.preOrderPrint();
		}

		if(this.right){
			this.right.preOrderPrint();
		}

	}

	postOrderPrint(){
		if(this.left){
			this.left.postOrderPrint();
		}

		if(this.right){
			this.right.postOrderPrint();
		}

		console.log(this.tala);	
	}

	lastNodeLeft(last = null){
		if(this.left){
			return this.left.lastNodeLeft(this);
		}else{
			last.left = null;
			return this.tala;
		}



	}

	lastNodeRight(last = null){
		if(this.right){
			return this.right.lastNodeRight(this);
		}else{
			last.right = null;
			return this.tala;
		}
	}

	delete(n, upp){
		if(n == this.tala){
			if(upp){
				this.tala = this.lastNodeLeft(this);
			}else{
				this.tala = this.lastNodeRight(this);
			}

		}else if(n > this.tala){
			if(this.right){
				this.right.delete(n);
			}else{
				return -1;
			};

		}else if(n < this.tala){
			if(this.left){
				this.left.delete(n);
			}else{
				return -1;
			}
		}
	}




}

class Tree{
	constructor(){
		this.head = null;
	}

	insert(tala){
		if(this.head){
			this.head.insert(tala);
		}else{
			this.head = new Node(tala);
		}
	}

	print(){
		if(this.head){
			this.head.print();
		}else{
			console.log("Ekkert í Tré");
		}
	}

	preOrderPrint(){
		if(this.head){
			this.head.preOrderPrint();
		}else{
			console.log("Ekkert í Tré");
		}
	}

	postOrderPrint(){
		if(this.head){
			this.head.postOrderPrint();
		}else{
			console.log("Ekkert í Tré");
		}
	}

	delete(n){
		if(this.head.tala == n){
			if(this.head.right && this.head.left){
				this.head.tala = this.head.right.lastNodeLeft();

			}else if(this.head.right){
				this.head = this.head.right;
			}else if(this.head.left){
				this.head = this.head.left;
			}else{
				this.head = null;
			}

		}else{
			if(n < this.head.tala){
				this.head.delete(n, false);
			}else if(n > head.tala){
				this.head.delete(n, true);

			}
		}
	}

	deleteTree(){
		this.head = null;
	}

}


tree = new Tree();

tree.insert(10);
tree.insert(5);
tree.insert(3);
tree.insert(4);
tree.insert(8);
tree.insert(6);
tree.insert(9);
tree.insert(20);
tree.insert(15);

tree.postOrderPrint();
console.log("-------------")
tree.delete(8);
tree.postOrderPrint();