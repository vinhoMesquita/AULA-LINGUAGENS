#include <iostream>
#include <string>

using namespace std;
//ler o nome e o sobrenime, exibir o sobrenome e a primeira letra do nome e a ultima
int main(){
    
    string nome;

    string sobreNome;

    cout <<"Digite seu nome: " << endl;
    cin >> nome;

    cout <<"Digite seu sobre-nome: " << endl;
    cin >> sobreNome;

    int tamanho = nome.size();

    cout << sobreNome << ", "<< nome[0]<<", " << nome[tamanho-1] << endl;  






    return 0;
}