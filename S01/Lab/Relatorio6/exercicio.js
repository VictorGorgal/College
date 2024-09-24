class Animal {
    constructor(nome, especie, idade) {
        this.nome = nome;
        this.idade = idade;
        this.especie = especie;
    }

    printInfo() {
        console.log(`Nome: ${this.nome}, Espécie: ${this.especie}, Idade: ${this.idade}`);
    }
}

class Gato extends Animal {
    constructor(nome, idade, cores, especie) {
        super(nome, idade, especie);
        this.cores = cores;  
    }

    printInfo() {
        console.log(`Cores: ${this.cores.join(', ')}`);
    }
}

class Cachorro extends Animal {
    constructor(nome, idade, raca, especie) {
        super(nome, idade, especie);
        this._raca = raca; 
    }

    printInfo() {
        console.log(`Raça: ${this._raca}`);
    }
}

const animal = new Animal("Pinguin", "Ave", 3);
const gato = new Gato("Teremia", 12, ["Laranja"], "Felino");
const cachorro = new Cachorro("Batolomeu", 11, "Labrador", "Cachorro");

animal.printInfo();
console.log("\n");
gato.printInfo();
console.log("\n");
cachorro.printInfo();
