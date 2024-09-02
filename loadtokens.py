import subprocess

def get_pass(entry: str):
    token = subprocess.run(['pass', 'show', entry], stdout=subprocess.PIPE, text=True)
    return token.stdout.strip()

OPENROUTER_API_KEY = get_pass('hermes/openrouter')
DISCORD_TOKEN = get_pass('hermes/bottoken')

