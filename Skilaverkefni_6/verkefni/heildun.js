
class FlatarMalHeildun{
	constructor(f,g,x1,x2){
		this.f = f;
		this.g = g;
		this.x1 = x1;
		this.x2 = x2;
		this.F = this.helda(this.f);
		this.G = this.helda(this.g);
	};

	helda(f){
		let hluti = "";
		let indexHluti = "";
		let hlutiList = [];
		let F = "";
		for(let i in f){
	    	if(f[i] != "+" && f[i] != "-" && f[i] != "x"){
	    		hluti += f[i];
	    	}else if(f[i] == "x"){
	    		if(hluti)
	    			hlutiList.push(hluti);
			   		hluti = ""
			   	if(hlutiList[0]){
					hlutiList.push("x");
			   	}else{
			   		hlutiList.push("1");
			   		hlutiList.push("x");
			   	
			   	}

	    	}else{
	    		if(hluti)
	    			hlutiList.push(hluti);
	    			hluti = "";
	    		hlutiList.push(" ");
	    	}
	    	if(hluti){
	    		hlutiList.push(hluti);
	    		hluti = "";
	    	}else{
	    		hlutiList.push("1");
	    	}
		
	    	
		}
		



		// F = "(" +hlutiList[0] +"/"+ (parseInt(hlutiList[2]) +1) +")*"+ hlutiList[1]+"*" + (parseInt(hlutiList[2]) +1)  ;
		return hlutiList;

	}

	reikanaX(f,x){
		return (f[0]/f[2])*x**f[2];
	}

	get FlatarMal(){
		console.log("F: " + this.F)
		console.log("G: " + this.G)
		console.log(this.reikanaX(this.F, this.x1))
		console.log(this.reikanaX(this.F, this.x2))
		console.log(this.reikanaX(this.G, this.x1))
		console.log(this.reikanaX(this.G, this.x2))


		return Math.abs((this.reikanaX(this.F, this.x1)- this.reikanaX(this.F, this.x2)) - (this.reikanaX(this.G, this.x1)-this.reikanaX(this.G, this.x2)));
	}
		
}


flatarMal = new FlatarMalHeildun("-x2+5x-3","x", 3, 1);

console.log(flatarMal.FlatarMal);