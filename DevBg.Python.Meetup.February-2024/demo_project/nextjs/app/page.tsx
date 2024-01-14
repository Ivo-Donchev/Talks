'use client'
import { useEffect, useState } from 'react';
import { Container, Typography, Card, CardContent, makeStyles } from '@material-ui/core';

const useStyles = makeStyles({
  root: {
    marginTop: 20,
  },
  article: {
    marginBottom: 20,
  },
  comments: {
    marginTop: 20,
  },
});


export default function ArticleDetailPage() {
  const classes = useStyles();

  const [article, setArticle] = useState(null);
  const [comments, setComments] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const articleResponse = await fetch('http://localhost:8000/blog/articles/1/');
      const articleData = await articleResponse.json();
      setArticle(articleData);

      const commentsResponse = await fetch('http://localhost:8000/blog/articles/1/comments/');
      const commentsData = await commentsResponse.json();
      setComments(commentsData);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Container className={classes.root}>
      {article && (
        <Card className={classes.article}>
          <CardContent>
            <Typography variant="h5">{article.title}</Typography>
            <Typography variant="body1">{article.content}</Typography>
          </CardContent>
        </Card>
      )}

      {comments.length > 0 && (
        <div className={classes.comments}>
          <Typography variant="h6">Comments</Typography>
          {comments.map((comment) => (
            <Card key={comment.id}>
              <CardContent>
                <Typography variant="body1">{comment.content}</Typography>
                <Typography variant="body2">By: {comment.author}</Typography>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </Container>
  );
}
