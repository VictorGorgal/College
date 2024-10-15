using System;

public class Cachorro {
    public string Nome { get; set; }
    public int Idade { get; set; }

    public Cachorro(string nome, int idade) {
        Nome = nome;
        Idade = idade;
    }

    public void ShowNome() {
        Console.WriteLine($"O nome do cachorro é: {Nome}");
    }

    public virtual void ShowIdade() {
        Console.WriteLine($"A idade do cachorro é: {Idade}");
    }
}

public class CachorroGrande : Cachorro {
    private string Tamanho = "Grande";

    public CachorroGrande(string nome, int idade) : base(nome, idade) {

    }

    public override void ShowIdade() {
        Console.WriteLine($"Este é um cachorro grande. A idade dele é: {Idade} anos.");
    }

    public void ShowTamanho() {
        Console.WriteLine($"O tamanho do cachorro é: {Tamanho}");
    }
}

public class CachorroPequeno : Cachorro {
    public CachorroPequeno(string nome, int idade) : base(nome, idade) {
    }

    public override void ShowIdade() {
        Console.WriteLine($"Este é um cachorro pequeno. A idade dele é: {Idade} anos.");
    }
}

class Program {
    static void Main(string[] args) {
        Cachorro cachorroNormal = new Cachorro("Cachorro normal", 4);
        cachorroNormal.ShowNome();
        cachorroNormal.ShowIdade();
        Console.WriteLine();

        CachorroGrande cachorroGrande = new CachorroGrande("Cachorro grande", 8);
        cachorroGrande.ShowNome();
        cachorroGrande.ShowIdade();
        cachorroGrande.ShowTamanho();
        Console.WriteLine();

        CachorroPequeno cachorroPequeno = new CachorroPequeno("Cachorro pequeno", 1);
        cachorroPequeno.ShowNome();
        cachorroPequeno.ShowIdade();
        Console.WriteLine();
    }
}
