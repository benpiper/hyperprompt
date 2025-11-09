# Hyperprompt

## How it works

Prompts are often not well defined, but LLMs have an uncanny ability to rephrase the query and add more detail, effectively enriching it.

Hyperprompt takes a simple user-defined prompt and combines it with a specially crafted system prompt to yield a better prompt--a hyperprompt!


## How to use

Set the environment variable OPENAI_API_KEY.

Modify the `USER_PROMPT` to the prompt you want to optimize.

```sh
pipenv shell
pipenv install -r requirements.txt
python3 hyperprompt.py
```

## Examples

Hyperprompt will try to stay true to the original prompt. 

### User prompt 1:
```
my friend gave me some green tea balls. how do i make tea like this. I like iced tea. My friend is really nice and loves tea, but I like coffee. I want to try green tea but I heard it causes heartburn. I have heartburn and don't want to make it worse but I don't want to offend my friend.
```

### Hyperprompt 1:
```
Explain how to make iced green tea using tea balls, with a practical, step-by-step method for a smooth brew. Include guidance on choosing tea balls, water temperature, steeping time, sweetness, and serving ideas for iced tea. Address heartburn concerns by outlining low-acid, lower-caffeine options and gentle preparation tweaks to minimize discomfort, plus safe alternatives. Also offer etiquette-friendly ideas for enjoying tea with a friend who loves tea while you prefer coffee, including phrases to express appreciation without offending.
```

---

### User prompt 2:
```
make green tea from pellets
```

### Hyperprompt 2:
```
Describe a practical, step-by-step method for brewing green tea starting from tea pellets. Include preparation of pellets, water temperature, infusion time, leaf-to-water ratio, recommended equipment, and tips to maximize aroma and flavor.
```

---

### User prompt 3:
```
make python flask app with JS and a contact form
```

### Hyperprompt 3:
```
Create a minimal Flask-based web app with a frontend using JavaScript that presents a contact form, handles submissions at a dedicated route, performs validation on both client and server sides, provides user feedback, and includes a clean project structure with templates and static assets.
```