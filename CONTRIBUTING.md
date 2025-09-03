    # Contributing to Helix Anomalous Math Training

    We welcome contributions to enhance our dataset of anomalous math problems! Follow these guidelines to contribute effectively.

    ## How to Contribute
    - **Suggest Anomaly Types**: Propose new categories (e.g., paradox, symbolic-confusion) via GitHub Issues.
    - **Add Problems**: Submit problems in JSON format, following `docs/schema.yaml` (e.g., include `explanation_goals`, `tags` like `clone-trap`).
    - **Write Explanations**: Solutions must be step-by-step, addressing `dispel-pattern`, `causal-mechanism`, or `counterexample-needed`.
    - **Submit PRs**: Target the `dev` branch. Include a Minimal Card:
      ```markdown
      ---
      Title: [Your PR Title]
      Date/UTC: [YYYY-MM-DDTHH:MMZ]
      Owner: [Your GitHub Handle]
      BLUF: [One-sentence summary]
      - [Bullet points of changes]
      Evidence: [Link to PR or issue]
      Needs verification: y
      Consent gate (non-reversible?): y/n
      Next: [Next steps]
      Disconfirmer: [What would invalidate this PR]
      Purpose: [Why this change matters]
      ---
      ```
    - **Report Issues**: Use GitHub Issues for bugs or suggestions.

    ## Code of Conduct
    Be respectful, collaborative, and focus on explanatory depth.

    ## License
    Contributions are licensed under Apache 2.0. See `LICENSE` for details.

    ## Questions?
    Open an issue or join our community (link TBD).
    ```

