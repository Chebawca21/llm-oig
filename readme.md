# Zadanie olimpiady informatycznej

## Zapisy konwersacji z ChatGPT

### Liczby królewskie (krolewskie)

* [Zero shot](https://chat.openai.com/share/0e48a53f-1f03-44d2-a57c-d604a041e499)

* [Chain-of-Thoughts](https://chat.openai.com/share/351d304e-c711-41b8-a1d0-ffeb7493335f)

* [Audience](https://chat.openai.com/share/034674c9-fe98-4288-bf44-3e222cc6b7e6)

* [Audience with Chain-of-Thoughts](https://chat.openai.com/share/a4df69ce-5b43-4e97-8db8-15ed75b66bdb)

* [Generated Knowledge](https://chat.openai.com/share/eeb262f1-d2bd-4cd9-b535-1ff6c20ec9a6)

### Mistrzostwa (mistrzostwa)

* [Zero shot](https://chat.openai.com/share/43acabc4-cfad-453e-92a0-1f59540cd9e3)

* [Chain-of-Thoughts](https://chat.openai.com/share/4be93da9-b68b-46a3-a889-5ce5d67c241e)

* [Audience](https://chat.openai.com/share/750ff2fd-8158-4550-96f4-a56bde37193c)

* [Audience with Chain-of-Thoughts](https://chat.openai.com/share/92c57289-174e-4323-b46e-bed38f4e45e2)

* [Generated Knowledge](https://chat.openai.com/share/6d9a5a77-b8bb-4585-81ae-fb53711c3a14)

### Listonosz (listonosz)

* [Zero shot](https://chat.openai.com/share/8b5af078-41d8-40f7-9715-d1a17eef97b3)

* [Chain-of-Thoughts](https://chat.openai.com/share/0f7e7e4e-6d0b-49bb-ba1e-620dacb67d8f)

* [Audience](https://chat.openai.com/share/7a25cbe1-5b27-48b2-8f51-441faa0afbb6)

* [Audience with Chain-of-Thoughts](https://chat.openai.com/share/101cb783-d2d0-4e0c-96e1-4a31e798afe7)

* [Generated Knowledge](https://chat.openai.com/share/a4a43ed8-3be5-4b7e-8642-b836a248e0b3)

### Wskaźnik Hirscha (wsk)

* [Zero shot](https://chat.openai.com/share/071babba-5648-4911-b612-ea0219b94441)

* [Chain-of-Thoughts](https://chat.openai.com/share/fc34a781-b0fb-4724-8b1a-bd0408c7679a)

* [Audience](https://chat.openai.com/share/5f300511-c015-4c71-be24-07806c073b70)

* [Audience with Chain-of-Thoughts](https://chat.openai.com/share/482a333f-9b06-4b28-95f5-b572a9df1898)

* [Generated Knowledge]()

### Regał (regal)

* [Zero shot](https://chat.openai.com/share/0e45a618-86e7-49c6-8b8c-9a791e5afd97)

* [Chain-of-Thoughts](https://chat.openai.com/share/a1ba9b19-9ae3-4d7c-8b4d-e0bd0e78fb44)

* [Audience](https://chat.openai.com/share/505a56df-de44-4753-8627-021e70512a93)

* [Audience with Chain-of-Thoughts](https://chat.openai.com/share/0f93fc07-199f-46d0-86ea-e295eee83a1c)

* [Generated Knowledge](https://chat.openai.com/share/bf99b647-c231-438d-9f4c-18a25c909050)

### Pranie (pranie)

* [Zero shot](https://chat.openai.com/share/fd90bb89-dca1-4e01-8976-90e7d7d481bf)

* [Chain-of-Thoughts](https://chat.openai.com/share/9f12cf06-a21b-40bc-90de-b20e9631cd69)

* [Audience](https://chat.openai.com/share/fc74858a-e8a7-435c-8408-f36b24f3df9c)

* [Audience with Chain-of-Thoughts](https://chat.openai.com/share/4e652bd6-4ef0-478d-815a-1288f630a562)

* [Generated Knowledge](https://chat.openai.com/share/2352ee31-f8ba-464b-9fbb-7610c17376bb)

### Kolorowy wąż (waz)

* [Zero shot](https://chat.openai.com/share/6a62dc35-1699-4851-93fa-a906929644c4)

* [Chain-of-Thoughts](https://chat.openai.com/share/b2d359f9-e6fb-48e9-b908-26e9f67408d7)

* [Audience](https://chat.openai.com/share/df3f160d-6fc8-4a0e-9ee8-86b174180a9d)

* [Audience with Chain-of-Thoughts](https://chat.openai.com/share/fb606e53-9416-46ab-b8f3-378ba6307b51)

* [Generated Knowledge]()


## Uzyskane wyniki

| Zadanie                   | Zero-shot   | COT        | Audience    | Audience with COT | Generated knowledge
| ------------------------- | ----------- |----------- | ----------- | -----------       | -----------
| Liczby królewskie         | 0/100       | 12/100     | 0/100       | 12/100            | 12/100
| Mistrzostwa               | 0/100       | 0/100      | 0/100       | 100/100           | 100/100
| Listonosz                 | 80/100      | 80/100     | 80/100      | 80/100            | 80/100
| Wskaźnik Hirscha          | 0/100       | 0/100      | 0/100       | 0/100             |
| Regał                     | 0/100       | 48/100     | 100/100     | 100/100           | 100/100
| Pranie                    | 0/100       | 50/100     | 50/100      | 50/100            | 50/100
| Kolorowy wąż              | 0/100       | 0/100      | 0/100       | 0/100             |

## p-value

Regał

| Numer wykonania  | Zero-shot   | COT        | Audience    | Audience with COT | Generated knowledge
| ---------------- | ----------- |----------- | ----------- | -----------       | -----------
| 1                | 0/100       | 48/100     | 87/100      | 87/100            | 100/100
| 2                | 100/100     | 100/100    | 100/100     | 100/100           | 100/100
| 3                | 48/100      | 100/100    | 100/100     | 48/100            | 100/100
| 4                | 100/100     | 100/100    | 48/100      | 100/100           | 100/100
| 5                | 100/100     | 48/100     | 48/100      | 48/100            | 100/100
| 6                | 100/100     | 100/100    | 100/100     | 100/100           | 100/100
| 7                | 100/100     | 0/100      | 100/100     | 12/100            | 100/100
| 8                | 100/100     | 48/100     | 100/100     | 100/100           | 100/100
| 9                | 100/100     | 100/100    | 100/100     | 100/100           | 100/100
| 10               | 48/100      | 100/100    | 100/100     | 100/100           | 100/100

| Statystyka                 | Zero-shot | COT    | Audience | Audience with COT | Generated knowledge
| -------------------------- | ----------|------- | -------- | -----------       | -----------
| Średnia arytmetyczna       | 79.6      | 74.4   | 88.3     | 79.5              | 100
| Odchylenie standardowe     | 33.54     | 34.0   | 20.51    | 30.2              | 0

| p-value             | Zero-shot | COT    | Audience | Audience with COT | Generated knowledge
| ------------------- | ----------|------- | -------- | -----------       | -----------
| Zero-shot           | -         | 0.735  | 0.495    | 0.994             | 0.087
| COT                 | 0.735     | -      | 0.286    | 0.727             | 0.041
| Audience            | 0.495     | 0.286  | -        | 0.457             | 0.105
| Audience with COT   | 0.994     | 0.727  | 0.457    | -                 | 0.060
| Generated knowledge | 0.087     | 0.041  | 0.105    | 0.060             | -

Liczby królewskie

| Numer wykonania  | Zero-shot   | COT        | Audience    | Audience with COT | Generated knowledge
| ---------------- | ----------- |----------- | ----------- | -----------       | -----------
| 1                | 48/100      | 48/100     | 0/100       | 12/100            | 12/100
| 2                | 48/100      | 24/100     | 0/100       | 48/100            | 12/100
| 3                | 0/100       | 48/100     | 0/100       | 48/100            | 12/100
| 4                | 48/100      | 48/100     | 0/100       | 48/100            | 12/100
| 5                | 24/100      | 48/100     | 48/100      | 48/100            | 12/100
| 6                | 0/100       | 12/100     | 0/100       | 36/100            | 12/100
| 7                | 48/100      | 48/100     | 0/100       | 48/100            | 12/100
| 8                | 0/100       | 48/100     | 0/100       | 48/100            | 12/100
| 9                | 48/100      | 48/100     | 0/100       | 12/100            | 0/100
| 10               | 48/100      | 12/100     | 0/100       | 0/100             | 12/100

| Statystyka                 | Zero-shot | COT    | Audience | Audience with COT | Generated knowledge
| -------------------------- | ----------|------- | -------- | -----------       | -----------
| Średnia arytmetyczna       | 31.2      | 38.4   | 4.8      | 34.8              | 10.8
| Odchylenie standardowe     | 21.6      | 14.99  | 14.4     | 18.16             | 3.6

| p-value             | Zero-shot | COT    | Audience | Audience with COT | Generated knowledge
| ------------------- | ----------|------- | -------- | -----------       | -----------
| Zero-shot           | -         | 0.167  | 0.006    | 0.692             | 0.015
| COT                 | 0.167     | -      | 0.001    | 0.635             | 0.001
| Audience            | 0.006     | 0.001  | -        | 0.001             | 0.230
| Audience with COT   | 0.692     | 0.635  | 0.001    | -                 | 0.002
| Generated knowledge | 0.015     | 0.001  | 0.230    | 0.002             | -