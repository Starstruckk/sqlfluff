"""A list of db2 keywords."""

UNRESERVED_KEYWORDS = [
    # https://www.ibm.com/docs/en/db2/11.5?topic=sql-reserved-schema-names-reserved-words
    "ACTIVATE",
    "ADD",
    "AFTER",
    "AGE",
    "ALIAS",
    "ALL",
    "ALLOCATE",
    "ALLOW",
    "ALTER",
    "AND",
    "ANY",
    "AS",
    "ASENSITIVE",
    "ASSOCIATE",
    "ASUTIME",
    "ASYNCHRONY",
    "AT",
    "ATTRIBUTES",
    "AUDIT",
    "AUTHORIZATION",
    "AUX",
    "AUXILIARY",
    "BEFORE",
    "BEGIN",
    "BETWEEN",
    "BINARY",
    "BUFFERPOOL",
    "BUSINESS_TIME",
    "BY",
    "CACHE",
    "CALL",
    "CALLED",
    "CAPTURE",
    "CARDINALITY",
    "CASCADED",
    "CASE",
    "CAST",
    "CCSID",
    "CHAR",
    "CHARACTER",
    "CHECK",
    "CLIENT_ACCTNG",
    "CLIENT_APPLNAME",
    "CLIENT_USERID",
    "CLIENT_WRKSTNNAME",
    "CLONE",
    "CLOSE",
    "CLUSTER",
    "COLLECTION",
    "COLLID",
    "COLUMN",
    "COMMENT",
    "COMMIT",
    "CONCAT",
    "CONDITION",
    "CONNECT",
    "CONNECTION",
    "CONSTRAINT",
    "CONTAINS",
    "CONTINUE",
    "COUNT",
    "COUNT_BIG",
    "CREATE",
    "CROSS",
    "CURRENT",
    "CURRENT_DATE",
    "CURRENT_LC_CTYPE",
    "CURRENT_PATH",
    "CURRENT_SCHEMA",
    "CURRENT_SERVER",
    "CURRENT_TIME",
    "CURRENT_TIMESTAMP",
    "CURRENT_TIMEZONE",
    "CURRENT_USER",
    "CURSOR",
    "CYCLE",
    "DATA",
    "DATABASE",
    "DATAPARTITIONNAME",
    "DATAPARTITIONNUM",
    "DATE",
    "DAY",
    "DAYS",
    "DB2GENERAL",
    "DB2GENRL",
    "DB2SQL",
    "DBINFO",
    "DBPARTITIONNAME",
    "DBPARTITIONNUM",
    "DEALLOCATE",
    "DECFLOAT",
    "DECLARE",
    "DEFAULT",
    "DEFAULTS",
    "DEFINITION",
    "DELETE",
    "DENSERANK",
    "DENSE_RANK",
    "DESCRIBE",
    "DESCRIPTOR",
    "DETAILED",
    "DETERMINISTIC",
    "DIAGNOSTICS",
    "DISABLE",
    "DISALLOW",
    "DISCONNECT",
    "DISTINCT",
    "DISTRIBUTE",
    "DO",
    "DOCUMENT",
    "DOUBLE",
    "DROP",
    "DSSIZE",
    "DYNAMIC",
    "EACH",
    "EDITPROC",
    "ELSE",
    "ELSEIF",
    "ENABLE",
    "ENCODING",
    "ENCRYPTION",
    "END",
    "END-EXEC",
    "ENDING",
    "ERASE",
    "ESCAPE",
    "EVERY",
    "EXCEPT",
    "EXCEPTION",
    "EXCLUDING",
    "EXCLUSIVE",
    "EXECUTE",
    "EXISTS",
    "EXIT",
    "EXPLAIN",
    "EXTEND",
    "EXTENDED",
    "EXTERNAL",
    "EXTRACT",
    "FEDERATED",
    "FENCED",
    "FETCH",
    "FIELDPROC",
    "FILE",
    "FINAL",
    "FIRST",
    "FOR",
    "FOREIGN",
    "FREE",
    "FROM",
    "FULL",
    "FUNCTION",
    "GENERAL",
    "GENERATE",
    "GENERATED",
    "GET",
    "GLOBAL",
    "GO",
    "GOTO",
    "GRANT",
    "GRAPHIC",
    "GROUP",
    "HANDLER",
    "HASH",
    "HASHED_VALUE",
    "HAVING",
    "HIGH",
    "HINT",
    "HOLD",
    "HOUR",
    "HOURS",
    "IDENTITY",
    "IF",
    "IMMEDIATE",
    "IMPORT",
    "IN",
    "INCLUDING",
    "INCLUSIVE",
    "INCREMENT",
    "INDEX",
    "INDICATOR",
    "INDICATORS",
    "INF",
    "INFINITY",
    "INHERIT",
    "INNER",
    "INOUT",
    "INSENSITIVE",
    "INSERT",
    "INTEGRITY",
    "INTERSECT",
    "INTO",
    "IS",
    "ISNULL",
    "ISOBID",
    "ISOLATION",
    "ITERATE",
    "JAR",
    "JAVA",
    "JOIN",
    "KEEP",
    "KEY",
    "LABEL",
    "LANGUAGE",
    "LAST",
    "LATERAL",
    "LC_CTYPE",
    "LC_MESSAGES",
    "LC_TIME",
    "LEAVE",
    "LEFT",
    "LEVEL2",
    "LIKE",
    "LIMIT",
    "LINKTYPE",
    "LOCAL",
    "LOCALDATE",
    "LOCALE",
    "LOCALTIME",
    "LOCALTIMESTAMP",
    "LOCATOR",
    "LOCATORS",
    "LOCK",
    "LOCKMAX",
    "LOCKSIZE",
    "LOGGED",
    "LONG",
    "LOOP",
    "LOW",
    "MAINTAINED",
    "MATERIALIZED",
    "MAXVALUE",
    "MDC",
    "MICROSECOND",
    "MICROSECONDS",
    "MINPCTUSED",
    "MINUS",
    "MINUTE",
    "MINUTES",
    "MINVALUE",
    "MODE",
    "MODIFIES",
    "MONTH",
    "MONTHS",
    "NAN",
    "NEW",
    "NEW_TABLE",
    "NEXTVAL",
    "NO",
    "NOCACHE",
    "NOCYCLE",
    "NODENAME",
    "NODENUMBER",
    "NOMAXVALUE",
    "NOMINVALUE",
    "NONE",
    "NOORDER",
    "NORMALIZED",
    "NOT",
    "NOTNULL",
    "NULL",
    "NULLS",
    "NUMPARTS",
    "OBID",
    "OF",
    "OFF",
    "OFFSET",
    "OLD",
    "OLD_TABLE",
    "ON",
    "OPEN",
    "OPTIMIZATION",
    "OPTIMIZE",
    "OPTION",
    "OR",
    "ORDER",
    "ORGANIZE",
    "OUT",
    "OUTER",
    "OVER",
    "OVERRIDING",
    "PACKAGE",
    "PADDED",
    "PAGE",
    "PAGESIZE",
    "PARAMETER",
    "PART",
    "PARTITION",
    "PARTITIONED",
    "PARTITIONING",
    "PARTITIONS",
    "PASSWORD",
    "PATH",
    "PERCENT",
    "PIECESIZE",
    "PLAN",
    "POSITION",
    "PRECISION",
    "PREPARE",
    "PREVVAL",
    "PRIMARY",
    "PRIQTY",
    "PRIVILEGES",
    "PROCEDURE",
    "PROFILE",
    "PROGRAM",
    "PSID",
    "PUBLIC",
    "QUERY",
    "QUERYNO",
    "RANDOM",
    "RANGE",
    "RANK",
    "READ",
    "READS",
    "RECOVERY",
    "REFERENCES",
    "REFERENCING",
    "REFRESH",
    "REJECT",
    "RELEASE",
    "RENAME",
    "REPEAT",
    "RESET",
    "RESIGNAL",
    "RESTART",
    "RESTRICT",
    "RESULT",
    "RESULT_SET_LOCATOR",
    "RETURN",
    "RETURNS",
    "REVERSE",
    "REVOKE",
    "RIGHT",
    "ROLE",
    "ROLLBACK",
    "ROLLOUT",
    "ROUND_CEILING",
    "ROUND_DOWN",
    "ROUND_FLOOR",
    "ROUND_HALF_DOWN",
    "ROUND_HALF_EVEN",
    "ROUND_HALF_UP",
    "ROUND_UP",
    "ROUNDING",
    "ROUTINE",
    "ROW",
    "ROWNUMBER",
    "ROWS",
    "ROWSET",
    "ROW_NUMBER",
    "RRN",
    "RUN",
    "SAVEPOINT",
    "SAMPLED",
    "SCANS",
    "SCHEMA",
    "SCRATCHPAD",
    "SCROLL",
    "SEARCH",
    "SECOND",
    "SECONDS",
    "SECQTY",
    "SECURITY",
    "SELECT",
    "SENSITIVE",
    "SEQUENCE",
    "SESSION",
    "SESSION_USER",
    "SET",
    "SIGNAL",
    "SIMPLE",
    "SNAN",
    "SNAPSHOT",
    "SOME",
    "SOURCE",
    "SPECIFIC",
    "SPECIFICATION",
    "SPLIT",
    "SQL",
    "SQL_CCFLAGS",
    "SQLID",
    "STACKED",
    "STANDARD",
    "START",
    "STARTING",
    "STATEMENT",
    "STATIC",
    "STATMENT",
    "STAY",
    "STOGROUP",
    "STORES",
    "STYLE",
    "SUBSTRING",
    "SUMMARY",
    "SYNONYM",
    "SYSFUN",
    "SYSIBM",
    "SYSPROC",
    "SYSTEM",
    "SYSTEM_TIME",
    "SYSTEM_USER",
    "TABLE",
    "TABLESPACE",
    "TEMPORAL",
    "THEN",
    "TIME",
    "TIMEOUT",
    "TIMESTAMP",
    "TIMEZONE",
    "TO",
    "TRANSACTION",
    "TRIGGER",
    "TRIM",
    "TRUNCATE",
    "TYPE",
    "TYPES",
    "UNDO",
    "UNION",
    "UNIQUE",
    "UNTIL",
    "UNSAMPLED",
    "UPDATE",
    "USAGE",
    "USER",
    "USING",
    "VALIDPROC",
    "VALUE",
    "VALUES",
    "VARIABLE",
    "VARIANT",
    "VCAT",
    "VERSION",
    "VIEW",
    "VOLATILE",
    "VOLUMES",
    "WHEN",
    "WHENEVER",
    "WHERE",
    "WHILE",
    "WITH",
    "WITHOUT",
    "WLM",
    "WRITE",
    "XMLELEMENT",
    "XMLEXISTS",
    "XMLNAMESPACES",
    "XMLPARSE",
    "XMLPATTERN",
    "YEAR",
    "YEARS",
    "YES",
]
