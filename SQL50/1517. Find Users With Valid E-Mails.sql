-- SELECT 
--     *
-- FROM Users
-- WHERE 
--     SUBSTRING_INDEX(mail, '@', 1) REGEXP '^[A-Za-z][A-Za-z0-9_.-]*$' AND
--     mail LIKE '%@leetcode.com' AND
--     LENGTH(mail) - CHAR_LENGTH(REPLACE(mail, '@', '')) = 1
    
SELECT
    *
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.-]*@leetcode\\.com$'
