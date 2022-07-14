# NTP Projekat
Odabrani projekat je predefinisani projekat - Kanonov algoritam za množenje matrica 

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


