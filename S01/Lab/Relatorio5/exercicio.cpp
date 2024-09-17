#include <iostream>
#include <string>

using namespace std;

class Pessoa {
    protected:
        string nome;
        int idade;

    public:
        Pessoa(string nome, int idade) {
            this->nome = nome;
            this->idade = idade;
        }

        void mostrarNome() {
            cout << "Nome: " << nome << endl;
        }

        virtual void mostrarIdade() {
            cout << "Idade: " << idade << endl;
        }
};

class Aluno : public Pessoa {
    private:
        string matricula;

    public:
        Aluno(string nome, int idade, string matricula) : Pessoa(nome, idade) {
            this->matricula = matricula;
        }

        void mostrarIdade() override {
            cout << "Idade do aluno: " << idade << endl;
        }

        void mostrarMatricula() {
            cout << "Matricula: " << matricula << endl;
        }
};

class Professor : public Pessoa {
    public:
        Professor(string nome, int idade) : Pessoa(nome, idade) {

        }

        void mostrarIdade() override {
            cout << "Idade do professor: " << idade << endl;
        }
};

int main() {
    Pessoa pessoa("Pessoa 1", 18);
    Aluno aluno("Aluno", 14, "5555");
    Professor professor("Professor", 62);

    pessoa.mostrarNome();
    pessoa.mostrarIdade();

    aluno.mostrarIdade();
    aluno.mostrarNome();
    aluno.mostrarMatricula();

    professor.mostrarNome();
    professor.mostrarIdade();

    return 0;
}
