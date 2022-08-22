# Kanonov algoritam za množenje matrica - NTP Projekat

Odabran je predefinisani projekat - Kanonov algoritam za množenje matrica 

## Student
SW-37/2018 Nenad Petković

## Opis algoritma

Kanonov algoritam je distriburiani agoritam za množenje dvodimenzionih matrica. Glavna prednost ovog algoritma je što zahtevi za skladištenje ostaju konstantni i nezavisni od boja procesa.

## Kanonov algoritam 

1. Posmatramo dve n × n matrice A i B podeljene na p blokova.
2. A(i, j) i B(i, j) (0 ≤ i,j ≤ √p) veličine (n ∕ √p)×(n ∕ √p) svaki.
3. Proces P(i, j) u početku skladišti A(i, j), a B(i, j) izračunava blok C(i, j) matrice rezultata.
4. Početni korak algoritma odnosi se na poravnanje matrica.
5. Poravnjavamo blokove A i B na takav način da svaki proces može nezavisno da počne da množi svoje lokalne podmatrice.
6. Ovo se radi tako što se sve podmatrice A(i, j) pomeraju ulevo za i koraka, takođe sve podmatrice B(i, j) nagore za j koraka.
7. Izvršavamo množenje lokalnog bloka.
8. Svaki blok od A se pomera za jedan korak ulevo, a svaki blok od B se pomera za jedan korak gore.
9. Izvršavamo množenje sledećeg bloka, dodajemo delimičnom rezultatu, ponavljamo dok se svi blokovi ne pomnože.

![image](https://user-images.githubusercontent.com/70920836/179054881-4f32db86-e1ee-4d53-812d-13e9c3873cf0.png)

## Sekvencijalna implementacija algoritma

Pre iteracionog procesa izvršava se inicijalni šift matrica A i B. Zatim, u narednih p iteracija se množe matrice A i B, a rezultat dodaje u matricu C. Na kraju svake iteracije matrice A i B se šiftuju za 1 korak. Konačni rezultat je matrica C (C = A x B).

## Implementacija algoritama i tehnologije koje se korsite

Algoritam će biti implentiran paralelno i sekvencijalno u Golang-u i Python-u. Vršiće se slabo i jako skaliranje tako što će se meriti srednje vreme izvršavanja algoritma (u svim slučajevima). U Python-u će se koristiti navedena biblioteka multiprocessing. Sekvencijalno množenje će imitirati paralelno, tako da se rešenja mogu upoređivati.

## Vizualizacija rešenja

Svaka iteracija sekvencijalnog rešenja i svaki proces paralelnog rešenja biće vizualizovani pomoću programskog jezika Pharo. 
