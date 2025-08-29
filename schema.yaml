schema:
  fields:
    - name: id
      type: string
      required: true
      description: Unique identifier for the problem
    - name: category
      type: string
      required: true
      description: Problem category (e.g., arithmetic, algebra, geometry, logic, probability, creative, meta-cognitive)
    - name: problem
      type: string
      required: true
      description: Problem statement as plain text
    - name: solution
      type: string
      required: true
      description: Expected solution in plain text or structured form
    - name: tags
      type: list
      required: true
      description: List of tags describing the problem (e.g., paradox, combinatorial)
      default: []
    - name: difficulty
      type: string
      required: true
      description: Difficulty level (easy, medium, hard, challenge)
      default: "unknown"
    - name: answer
      type: any
      required: false
      description: Optional final answer (numeric, string, or object)
    - name: metadata
      type: object
      required: false
      description: Optional metadata with source, created_by, and date
      default: {}
      properties:
        - name: source
          type: string
          description: Source of the problem (human, synthetic, mixed)
        - name: created_by
          type: string
          description: Author or system that created the problem
        - name: date
          type: string
          description: Creation date (YYYY-MM-DD)
