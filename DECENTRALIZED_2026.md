# AI-Ticket 2.0 - Fully Decentralized (No GitHub Dependency)

**Date**: January 22, 2026  
**Status**: Planning  
**Branch**: feature/zos-rust-migration

## Key Insight

**We don't need GitHub anymore!**

- ZOS Server = GUI + API
- libp2p = P2P networking
- No rate limits
- No permissions needed
- Fully autonomous

## Architecture

```
┌─────────────────────────────────────────────────┐
│              ZOS Server (GUI)                   │
│  - Web UI for ticket management                │
│  - REST API                                     │
│  - WebSocket for real-time updates             │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│           libp2p Network Layer                  │
│  - Peer discovery                               │
│  - Ticket distribution                          │
│  - Reward settlement                            │
│  - No central authority                         │
└─────────────────────────────────────────────────┘
                      ↓
┌─────────────────────────────────────────────────┐
│         Local Storage (Nix Store)               │
│  - Tickets stored in /nix/store                 │
│  - Immutable, content-addressed                 │
│  - ZK proofs for all operations                 │
└─────────────────────────────────────────────────┘
```

## Benefits

1. **No Rate Limits** - Your own server, your rules
2. **No Permissions** - No GitHub API tokens needed
3. **Fully Decentralized** - libp2p P2P network
4. **Autonomous** - Runs independently
5. **Proven** - ZK proofs for everything
6. **Fast** - No external API calls

## New Stack

### Replace GitHub API → libp2p
```rust
// OLD: GitHub API (rate limited, needs token)
octocrab::instance().issues().create(...)

// NEW: libp2p (P2P, no limits)
swarm.behaviour_mut().ticket.create(...)
```

### Replace GitHub Issues → ZOS Tickets
```rust
// Stored in /nix/store, content-addressed
/nix/store/abc123-ticket-fix-parser.json
```

### Replace GitHub Actions → ZOS Server
```rust
// ZOS server handles everything
POST /api/tickets/create
GET  /api/tickets/list
POST /api/tickets/claim
POST /api/tickets/submit
```

## Dependencies

```toml
[dependencies]
# P2P networking
libp2p = "0.53"
libp2p-kad = "0.45"
libp2p-gossipsub = "0.46"

# Web server
axum = "0.7"
tower = "0.4"

# Storage
sled = "0.34"  # Embedded DB

# Crypto
ed25519-dalek = "2.1"  # Signing

# ZK proofs
risc0-zkvm = "0.21"  # ZK-STARK
```

## Migration Plan

### Phase 1: ZOS Server (Week 1)
- Build web UI for tickets
- REST API endpoints
- WebSocket for updates
- Store in /nix/store

### Phase 2: libp2p Integration (Week 2)
- Peer discovery (mDNS + Kademlia)
- Ticket gossip protocol
- Reward settlement
- No GitHub dependency

### Phase 3: Rust Rewrite (Week 3)
- Lift Python → Rust (same as before)
- But use libp2p instead of GitHub API
- Store tickets locally

### Phase 4: ZK Proofs (Week 4)
- Prove ticket creation
- Prove ticket completion
- Prove reward payment
- All verifiable without trust

## File Structure

```
ai-ticket/
├── flake.nix
├── Cargo.toml
├── src/
│   ├── main.rs           # Entry point
│   ├── server.rs         # ZOS web server
│   ├── p2p.rs            # libp2p networking
│   ├── ticket.rs         # Ticket management
│   ├── storage.rs        # Nix store integration
│   ├── rewards.rs        # Reward system
│   └── proofs.rs         # ZK proof generation
├── web/                  # Web UI (Svelte/React)
│   ├── src/
│   └── dist/
└── proofs/               # ZK circuits
```

## Usage

```bash
# Start ZOS server
ai-ticket serve --port 8080

# Web UI available at http://localhost:8080

# Create ticket (via API or UI)
curl -X POST http://localhost:8080/api/tickets/create \
  -d '{"task": "Fix parser bug"}'

# List tickets
curl http://localhost:8080/api/tickets/list

# Claim ticket
curl -X POST http://localhost:8080/api/tickets/claim/abc123

# Submit work
curl -X POST http://localhost:8080/api/tickets/submit/abc123 \
  -d '{"proof": "..."}'
```

## P2P Network

```bash
# Join network
ai-ticket p2p --bootstrap /ip4/1.2.3.4/tcp/4001/p2p/QmXXX

# Discover peers
ai-ticket p2p peers

# Sync tickets
ai-ticket p2p sync
```

## No GitHub Needed!

- ✅ No API tokens
- ✅ No rate limits
- ✅ No permissions
- ✅ No external dependencies
- ✅ Fully autonomous
- ✅ P2P decentralized
- ✅ ZK proven

## Timeline

- Week 1: ZOS server + web UI
- Week 2: libp2p integration
- Week 3: Rust rewrites
- Week 4: ZK proofs

**Total freedom. No gatekeepers. Pure math.** 🚀

## LiteLLM Integration

**Location**: `/home/mdupont/projects/agentartificial/devops/vendor/litellm`  
**Your fork**: https://github.com/jmikedupont2/openlightllm

### What is LiteLLM?

Unified LLM API proxy that:
- Calls all LLM APIs using OpenAI format
- Supports: Gemini, Claude, GPT-4, Bedrock, HuggingFace, etc.
- Built-in rate limiting and budgets
- Automatic fallback logic
- Your own proxy server

### Integration with AI-Ticket

```rust
// OLD: Direct Gemini calls (rate limited)
gemini_api::generate(prompt)

// NEW: LiteLLM proxy (unlimited, multi-provider)
litellm_client::complete(prompt)
// → Tries Gemini
// → Falls back to Claude
// → Falls back to GPT-4
// → Falls back to local model
```

### Architecture Update

```
AI-Ticket (Rust)
    ↓
LiteLLM Proxy (Your server)
    ↓
┌─────────────────────────────────┐
│  Gemini  │  Claude  │  GPT-4   │
│  Local   │  Bedrock │  Azure   │
└─────────────────────────────────┘
```

### Benefits

✅ **No Single Provider Lock-in** - Use any LLM  
✅ **Automatic Fallback** - If one fails, try next  
✅ **Rate Limit Management** - Built-in  
✅ **Cost Tracking** - Per-key budgets  
✅ **OpenAI Format** - Standard interface  

### Setup

```bash
# Start LiteLLM proxy
cd /home/mdupont/projects/agentartificial/devops/vendor/litellm
litellm --config config.yaml

# Configure AI-Ticket to use it
export LITELLM_URL=http://localhost:4000
ai-ticket serve --llm-proxy $LITELLM_URL
```

### Config Example

```yaml
# litellm config.yaml
model_list:
  - model_name: gpt-4
    litellm_params:
      model: gemini/gemini-pro
      api_key: $GEMINI_KEY
  
  - model_name: gpt-4
    litellm_params:
      model: claude-3-opus
      api_key: $CLAUDE_KEY
  
  - model_name: gpt-4
    litellm_params:
      model: gpt-4
      api_key: $OPENAI_KEY

router_settings:
  fallbacks: true
  retry_policy: exponential_backoff
```

### Rust Integration

```toml
[dependencies]
reqwest = "0.11"  # HTTP client for LiteLLM
```

```rust
// src/llm.rs
pub async fn generate(prompt: &str) -> Result<String> {
    let client = reqwest::Client::new();
    let res = client
        .post("http://localhost:4000/chat/completions")
        .json(&json!({
            "model": "gpt-4",
            "messages": [{"role": "user", "content": prompt}]
        }))
        .send()
        .await?;
    
    let data: Value = res.json().await?;
    Ok(data["choices"][0]["message"]["content"].as_str().unwrap().to_string())
}
```

**No more Gemini rate limits. Multi-provider fallback. Your own proxy.** 🚀
