# stereoIT s.r.o. — Infrastructure & Deployment Setup Guide

Follow these steps to configure your deployment pipelines and developer environments.

## 1. GitHub Repository Connection
Every commit on `main` will trigger an automated build. To connect your local environment to GitHub:
```bash
# 1. Initialize local repository
git init

# 2. Add files
git add .
git commit -m "chore: initial project blueprints"

# 3. Create GitHub repo (ensure GitHub CLI 'gh' is authenticated)
gh repo create stereoit-website --private --source=. --remote=origin --push
```

## 2. Cloudflare Pages & CDN Deployment
Cloudflare Pages hosts our static site globally. To link your GitHub repo:

1. **Sign in** to your [Cloudflare Dashboard](https://dash.cloudflare.com/).
2. Navigate to **Workers & Pages** -> **Create application** -> **Pages** -> **Connect to Git**.
3. Authorize your GitHub account and select the `stereoit-website` repository.
4. Set up the **Build configuration**:
   - **Framework preset**: `SvelteKit`
   - **Build command**: `npm run build` or `bun run build`
   - **Build output directory**: `.svelte-kit/cloudflare` (or `build` if using `@sveltejs/adapter-static`)
5. Click **Save and Deploy**. Every subsequent push to GitHub will automatically compile and publish the site.

### CDN Image Optimization & Edge Caching
To serve graphics and screenshots dynamically:
- Store visual assets in the `/static` folder (e.g. `/static/images/hero-grid.svg`).
- Cloudflare globally caches these assets at the edge. To maximize speed:
  - Turn on **Cloudflare Polish** (under speed settings) to automatically compress and convert images to AVIF or WebP on the fly.
  - For advanced programmatic delivery, use **Cloudflare Images** mapped to your custom domain.

## 3. Google Stitch MCP Config in Opencode
To enable your AI agent to utilize Google Stitch to create designs and screens directly inside the CLI:

### Step A: Obtain Your Google Stitch API Key
1. Sign in to your account at [stitch.withgoogle.com](https://stitch.withgoogle.com).
2. Go to [stitch.withgoogle.com/settings](https://stitch.withgoogle.com/settings) and generate an API key.

### Step B: Configure Opencode
Add the Stitch MCP server to your global config file `~/.opencode/opencode.json` (inside the `"mcp"` block):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "stitch": {
      "type": "remote",
      "url": "https://stitch.googleapis.com/mcp",
      "enabled": true,
      "headers": {
        "X-Goog-Api-Key": "YOUR_GOOGLE_STITCH_API_KEY"
      }
    }
  }
}
```
Replace `YOUR_GOOGLE_STITCH_API_KEY` with your actual Stitch API key.

### Stitch Project Resource Info
*   **Project Title**: stereoIT
*   **Project ID**: `12396157723984667173`
*   **Resource Format**: `projects/12396157723984667173`

### Step C: Optional Stitch Kit Setup
To install 35 specialized design-to-code skills (including Svelte 5 and shadcn converters):
```bash
npx @booplex/stitch-kit
```
